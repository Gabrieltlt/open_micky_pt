# 🧪 Simulação do MICKY

<div style="text-align: justify;">

Esta seção orienta você na execução do ambiente de simulação do MICKY utilizando Gazebo e ROS 2.

---

## Passo 1 — Iniciar o Gazebo

1. Abre o Gazebo Harmonic com o mundo `turtlebot3_world` e insere o robô MICKY na simulação.

```bash
ros2 launch micky_simulation gazebo.launch.py
```

Aguarde até que a interface gráfica do Gazebo esteja completamente carregada e o modelo do robô esteja visível no cenário.

---

## Passo 2 — Iniciar o SLAM

2. Em um **novo terminal**, inicie o nó de SLAM e o RViz:

```bash
ros2 launch micky_slam sim_slam.launch.py
```

O RViz será aberto exibindo o tópico `/map`. O mapa começa vazio e é construído conforme o robô se movimenta.

---

## Passo 3 — Controlar o Robô (Teleop)

3. Em um **terceiro terminal**, inicie o teleop com teclado:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

| Tecla | Ação |
|-------|------|
| `i` / `,` | Avançar / Recuar |
| `j` / `l` | Deslocar para esquerda / direita |
| `u` / `o` | Girar à esquerda / direita |
| `space` | Parar |
| `w` / `x` | Increase / Aumentar / diminuir velocidade linear |

Movimente o robô por todo o ambiente. O mapa no RViz será preenchido à medida que novas áreas forem escaneadas. Para melhores resultados, percorra pelo menos um ciclo completo no ambiente, permitindo que o `slam_toolbox` realize o fechamento de loop.

---

4. O robô pode ser visualizado e controlado via teleop, como mostrado abaixo:

<div align="center">
<video width="60%" controls>
  <source src="../../_static/videos/simulation.mp4" type="video/mp4">
</video>
</div>

## Passo 4 — Salvar o Mapa

Após mapear completamente o ambiente, execute em qualquer terminal:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/micky_map
```

Isso irá gerar dois arquivos:
- `~/your_map.pgm` — imagem do mapa de ocupação
- `~/your_map.yaml` — metadados (resolução, origem, limiares)

---

## Problemas Comuns

### Gazebo não abre / trava na inicialização

```bash
pkill -f gz_sim && pkill -f gzserver
unset IGN_PARTITION GZ_PARTITION
```

Em seguida, execute novamente o Passo 1.

### O mapa permanece vazio no RViz

1. Verifique se o LiDAR está publicando dados:
   ```bash
   ros2 topic echo /laser_scan_front
   # Expected: ~10 Hz
   ```
2. Movimente o robô — o `slam_toolbox` só registra uma nova leitura após o robô percorrer pelo menos **0,5 m**.

### O robô não se move

```bash
# Test the command manually
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist \
  "{linear: {x: 0.2, y: 0.0, z: 0.0}, angular: {z: 0.0}}" --once
```

Se o robô se mover no Gazebo, mas não via teleop, verifique se o terminal do teleop está em foco (a entrada do teclado é capturada nele).

</div>