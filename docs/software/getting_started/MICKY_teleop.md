# 🎮 Teleop do MICKY

<div style="text-align: justify;">

Esta seção orienta você na execução do controle manual (teleoperação) do MICKY.

---

## Teleop com Teclado

Após instalar todos os pacotes necessários, conecte a placa Arduino (já configurada conforme o guia de instalação) ao seu computador.

Em seguida, abra dois terminais.

---

No primeiro terminal, execute:

```bash
ros2 launch motors_controller motors_controller.launch.py
```

---

No segundo terminal, execute:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

---

Use as seguintes teclas para controlar o robô:

| Tecla | Ação |
|-------|------|
| `i` | Avançar |
| `,` | Recuar |
| `j` | Girar à esquerda |
| `l` | Girar à direita |
| `u` | Frente + esquerda |
| `o` | Frente + direita |
| `m` | Trás + esquerda |
| `.` | Trás + direita |
| `k` | Parar o robô |

---

## Teleop com Joystick

Também é possível controlar o robô utilizando um controle Logitech.

---

### Instalar Pacotes Necessários

```bash
sudo apt install ros-humble-joy ros-humble-teleop-twist-joy
```

---

### Conectar o Controle

Conecte o controle Logitech via USB ou Bluetooth e execute os comandos abaixo:

Para verificar se foi reconhecido:

```bash
ls /dev/input/js0
```

---

No primeiro terminal, execute:

```bash
ros2 launch motors_controller motors_controller.launch.py
```

---

No segundo terminal, execute:

```bash
ros2 run joy joy_node
```

---

No terceiro terminal, execute:

```bash
ros2 run teleop_twist_joy teleop_node
```

---

### Controles

- Analógico esquerdo → movimento linear (frente/trás e lateral)
- Analógico direito → rotação

</div>