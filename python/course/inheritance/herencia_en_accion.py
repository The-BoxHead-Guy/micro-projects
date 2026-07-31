import requests
from bs4 import BeautifulSoup


class ScraperBase:
    def __init__(self, url):
        self._url = url
        self._noticias = []
        self._timeout = 5

    # --- @property: acceso de solo lectura desde fuera ---

    @property
    def url(self):
        return self._url

    @property
    def noticias(self):
        return list(self._noticias)  # copia, no la lista real

    @property
    def total(self):
        return len(self._noticias)

    # --- método protegido, solo para uso interno y subclases ---

    def _obtener_html(self):
        response = requests.get(self._url, timeout=self._timeout)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    # --- método protegido para que las hijas guarden resultados ---

    def _guardar(self, items):
        if not isinstance(items, list):
            raise TypeError("Los resultados deben ser una lista")
        self._noticias = items

    def scrapear(self):
        raise NotImplementedError("Cada scraper debe implementar scrapear()")

    def mostrar(self):
        if not self._noticias:
            print("No hay resultados, ejecuta scrapear() primero")
            return
        for i, item in enumerate(self._noticias, 1):
            print(f"{i}. {item}")


class HackerNewsScraper(ScraperBase):
    def __init__(self):
        super().__init__("https://news.ycombinator.com")
        self._timeout = 8  # la hija puede ajustar el timeout

    def scrapear(self):
        soup = self._obtener_html()
        titulos = soup.select(".titleline > a")
        self._guardar([t.get_text() for t in titulos])  # usa el método protegido
        return self.noticias


class QuotesScraper(ScraperBase):
    def __init__(self):
        super().__init__("https://quotes.toscrape.com")

    def scrapear(self):
        soup = self._obtener_html()
        quotes = soup.select(".quote .text")
        autores = soup.select(".quote .author")
        resultados = [
            f'"{q.get_text()}" — {a.get_text()}' for q, a in zip(quotes, autores)
        ]
        self._guardar(resultados)
        return self.noticias


class ScraperConExporte(QuotesScraper):
    def __init__(self, archivo="resultado.txt"):
        super().__init__()
        self._archivo = archivo

    @property
    def archivo(self):
        return self._archivo

    def exportar(self):
        if self.total == 0:
            raise ValueError("Nada que exportar, ejecuta scrapear() primero")
        with open(self._archivo, "w", encoding="utf-8") as f:
            f.write("\n".join(self.noticias))
        print(f"Exportados {self.total} resultados a {self._archivo}")


hn = HackerNewsScraper()
# hn.url = "otro.com"
print(hn.url)

hn.scrapear()
print(hn.total)  # solo lectura
print(hn.noticias)  # copia, no la lista real
hn.mostrar()

q = ScraperConExporte("citas.txt")
q.scrapear()
q.exportar()
print(q.archivo)  # citas.txt, solo lectura
