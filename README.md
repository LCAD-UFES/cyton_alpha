# cyton_alpha

roslaunch cyton_alpha_bringup bringup.launch
roslaunch cyton_alpha_moveit_config moveit_cyton_alpha_sim.launch




Em construção...

Para o laser ficar posicionado corretamente, modifique no arquivo :

     ~/catkin_ws/src/PioneerModel/p3dx_description/pioneer3dx.xacro

na joint:"lms100_joint"

em origin mude para:

     <origin xyz="0.075 0 0.274" rpy="0 0 0" />

Se fez o pull recentemente no PioneerModel, a versão do Git já foi atualizada com essa alteração
	
## Para teste
     roslaunch cyton_alpha_gazebo tamandua_gazebo.launch

Adicionado pacotes MoveIt e gazebo.

   MoveIt: arquivos de configuração gerados pelo setup do MoveIt.
   
   gazebo: configuracao das transmissões, launch em desenvolvimento.

Adicionado ao cyton_alpha_description:

   xacro da estrutura.
   
   xacro juntando p3dx,cyton,knect(pacote pr2) e estrutura.

### Agradecimentos

https://github.com/SD-Robot-Vision

https://github.com/lara-unb


