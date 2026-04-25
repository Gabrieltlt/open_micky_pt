# ⬇️ Instalar o MICKY

<div style="text-align: justify;">

Para instalar o MICKY, siga os comandos abaixo.

---

## Requisitos

Certifique-se de que você possui os seguintes itens instalados:

* Ubuntu 22.04
* ROS 2 Humble
* Arduino IDE ou PlatformIO
* Gazebo Harmonic (ou Garden)

---

## Instalar o Controlador da Base do MICKY

Clone o repositório:

```bash
mkdir -p /micky_ws/src && cd micky_ws/src
git clone https://github.com/FBOTWork/micky_base_controller.git
cd micky_base_controller
```

---

## Configuração do Firmware

Faça o upload do firmware para o Arduino Mega:

1. Abra o arquivo de firmware:

```bash
firmware_micro_controller/firmware.ino
```

2. Conecte o Arduino

3. Configure na Arduino IDE:

* Placa: **Arduino Mega 2560**
* Porta: `/dev/ttyACM0` ou `/dev/ttyUSB0`

4. Clique **Upload**

---

## Configuração USB (udev)

Configure um nome de dispositivo persistente para o Arduino.

### Obter informações do dispositivo

```bash
udevadm info -a -n /dev/ttyACM0 | grep -E 'idVendor|idProduct|serial'
```

### Criar regra udev

```bash
sudo nano /etc/udev/rules.d/99-arduino_robo.rules
```

Adicione:

```bash
SUBSYSTEM=="tty", ATTRS{idVendor}=="2341", ATTRS{idProduct}=="0043", MODE="0666", SYMLINK+="arduino_robo"
```

### Recarregar regras

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

### Verificar dispositivo

```bash
ls /dev/arduino_robo
```

### (Opcional) Adicionar permissões ao usuário

```bash
sudo usermod -aG dialout $USER
```

Faça logout e login novamente após executar esse comando.

---

## Instalar a Simulação do MICKY

Navegue até o diretório src do workspace e clone o repositório:

```bash
cd ~/micky_ws/src
git clone https://github.com/FBOTWork/micky_simulation.git
```

Instale as dependências com rosdep:

```bash
cd ~/micky_ws
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

Instale os pacotes ROS 2 necessários:

```bash
sudo apt install -y \
  ros-humble-ros-gz-sim \
  ros-humble-ros-gz-bridge \
  ros-humble-robot-state-publisher \
  ros-humble-slam-toolbox \
  ros-humble-nav2-map-server \
  ros-humble-xacro \
  ros-humble-rviz2
```

---

## Compilando o Workspace

Execute **uma vez** após clonar ou modificar os pacotes:

```bash
cd ~/micky_ws
colcon build --symlink-install
source install/setup.bash
```

</div>