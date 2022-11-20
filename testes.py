from processador_imagem.utils import io,plot
from processador_imagem.processamento import combination, transformation

imagem1=io.read_image("ceu_amazonia.jpg")
imagem2=io.read_image("por_do_sol_mg.jpg")

plot.plot_image(imagem1)
plot.plot_image(imagem2)