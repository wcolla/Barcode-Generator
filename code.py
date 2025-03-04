import barcode
from barcode.writer import ImageWriter
from IPython.display import Image, display
import os

# Configurações personalizadas do código de barras
CONFIGURACOES = {
    'module_width': 0.4,    # Largura das barras
    'module_height': 15.0,   # Altura das barras
    'font_size': 12,        # Tamanho da fonte do número
    'text_distance': 5.0,   # Distância entre o número e as barras
    'quiet_zone': 6.0       # Margem ao redor do código
}

def validar_ean13(numero: str) -> bool:
    """Valida se o número atende aos requisitos do EAN13"""
    return len(numero) == 13 and numero.isdigit()

# Número deve ter 13 dígitos numéricos
barcode_number = '1234567890128'  # Número corrigido para 13 dígitos

if not validar_ean13(barcode_number):
    raise ValueError("Número inválido para EAN13. Deve conter exatamente 13 dígitos.")

try:
    # Criação do código de barras
    ean13 = barcode.get_barcode_class('ean13')
    barcode_image = ean13(barcode_number, writer=ImageWriter())
    
    # Salva a imagem com extensão explícita
    filename = barcode_image.save(
        'barcode_ean13',  # Nome do arquivo
        options=CONFIGURACOES  # Aplica as configurações
    )
    
    # Exibe informações de confirmação
    print(f"Código de barras gerado com sucesso em: {os.path.abspath(filename)}")
    
    # Exibição no notebook com ajuste de tamanho
    display(Image(filename=filename))

except barcode.errors.BarcodeError as e:
    print(f"Erro na geração do código de barras: {str(e)}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {str(e)}")
