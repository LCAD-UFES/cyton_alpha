Para rodar o node do cyton e suas dependências:

Para rodar o node com o cyton ligado:

#roslaunch cyton slam.launch
	Este launch irá iniciar o nodes:
	-> openni, publica as mensagens de nuvem de pontos e imagem rgb. 
	-> hardware, liga e controla o cyton.
	-> cyton_kinect, assina mensagem de nuvem de pontos e imagem rgb, publica um ponto (x y z) do mundo no tópico /kinect_points.
	Este launch também inicia a tf do kinect em relação ao mundo e do cyton em relação ao mundo.
	-> cyton_kinematics, Este node faz subscribe no tópico /cyton_kinect/point , faz o solver das juntas e manda para o cyton.

Para rodar o node com o cyton desligado:

#roslaunch cyton slam.launch robot_sim:=true

Para usar o cyton_kinematics:
->clicar com botão esquerdo do mouse + CTRL na junta fixa (qualquer junta acima da primeira)
->digite a e observe a junta ficar vermelha

->clicar com botão esquerdo do mouse + CTRL na junta (end effector)
->digite s e observe a junta ficar verde

->aperte i para mover o end effector livremente

->aperte ii para calcular a posicao das juntas a partir de um ponto 3d que é passado pela interface do ros/cyton_kinect
