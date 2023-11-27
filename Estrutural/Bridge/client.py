"""Module client do padrão Bridge."""
from abstraction_interface import IPiloto
from implementor_interface import IVeiculo
from concrete_implementor import Carro, Moto, Caminhao
from refined_abstraction import Piloto


piloto = Piloto.new(Carro.new())

piloto.toggle_ligar()
piloto.aumentar_velocidade()
piloto.aumentar_velocidade()
piloto.aumentar_velocidade()
piloto.aumentar_velocidade()
piloto.aumentar_velocidade()
piloto.diminuir_velocidade()
piloto.virar_a_direita()
piloto.virar_a_esquerda()
piloto.dar_re()
piloto.freiar()
piloto = Piloto.new(Caminhao.new())
piloto.toggle_ligar()
piloto.aumentar_velocidade()
piloto.aumentar_velocidade()
piloto.aumentar_velocidade()
piloto.aumentar_velocidade()
piloto.aumentar_velocidade()
piloto.diminuir_velocidade()
piloto.virar_a_direita()
piloto.virar_a_esquerda()
piloto.dar_re()
piloto.freiar()