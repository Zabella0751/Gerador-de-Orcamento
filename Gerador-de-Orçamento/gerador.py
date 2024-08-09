from fpdf import FPDF

horas_estimadas = input("Digite o total de horas estimadas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado para a conlcusão: ")

valor_total = int(horas_estimadas) * int(valor_hora) 

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

pdf.image("pagina-pdf.png", x=0, y=0)

pdf.text(117, 182, horas_estimadas)
pdf.text(117, 203, valor_hora)
pdf.text(117, 223, prazo)
pdf.text(117, 243, str(valor_total))

pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")