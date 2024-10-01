#importacao da biblioteca FLET
import flet as ft
from deep_translator import GoogleTranslator

#classe para personalizacao do botao
class MyButton(ft.ElevatedButton):
    def __init__(self, text, on_click=None):
        super().__init__(text=text, on_click=on_click)
        self.bgcolor = ft.colors.WHITE
        self.color = ft.colors.BLUE
        self.text = text

def main(page: ft.Page):
    def tradudizir_clicked(e):
        print('Traduzir clicked')

    def acao(e):
        texto.value = str(texto.value)
        tradutor = GoogleTranslator(source='auto', target='pt')

        texto_traduzido = tradutor.translate(texto)
        print(texto_traduzido)


        page.update()

    page.title = 'Tradutor'
    page.scroll = 'adaptive'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = '#F0F8FF'

    # Declaracao de Variaveis
    texto = ft.TextField(label='Digite aqui o texto a traduzir:', bgcolor = '#F8F8FF')
    result = ft.Text(size=18)
    textoOriginal = ft.Text(size=18)

    page.add(
        ft.Row(
            [ft.Text('Tradutor Online', size = 35, weight= 'bold', color='blue')],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [texto],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [MyButton("Traduzir", on_click=acao)],#adiconando o botao 'traduzir
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [result],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [result]
        )
    )

    page.update()

# execucao aplicativo
ft.app(target=main)
