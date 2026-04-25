# ⚙️ Sistema de Locomoção

<div style="text-align: justify;">

O MICKY utiliza um sistema de locomoção baseado em rodas Mecanum, permitindo movimento omnidirecional sem a necessidade de rotação do corpo do robô.

O sistema adota uma arquitetura de controle híbrida, na qual o processamento de alto nível é realizado em um computador executando **ROS 2 Humble**, enquanto o controle de baixo nível é realizado por hardware dedicado. Essa separação garante atuação dos motores em tempo real, mantendo flexibilidade para planejamento e tomada de decisão.

Esse tipo de arquitetura é amplamente utilizado em aplicações de robótica móvel, proporcionando maior manobrabilidade, escalabilidade e robustez do sistema.

---

## Configuração de Hardware

O controle dos motores é gerenciado por um **Arduino Mega 2560**, que se comunica com quatro **drivers TB6600**. Esses drivers são responsáveis pela atuação dos **motores de passo Nema 23**.

Para navegação e estimativa de estado, o robô utiliza sensores **MPU6050**, conectados por meio do barramento I2C.

---

## Cinemática do Robô

O robô utiliza **rodas Mecanum**, permitindo movimento omnidirecional por meio da combinação das velocidades individuais de cada roda.

A cinemática do sistema é baseada na conversão dos comandos de velocidade do robô, definidos pelas velocidades lineares nos eixos X (`v_x`) e Y (`v_y`), juntamente com a velocidade angular (`ω`), em velocidades individuais das rodas.

Isso permite:

- Movimento para frente e para trás
- Movimento lateral (deslocamento lateral)
- Rotação
- Movimentos combinados (por exemplo, movimento diagonal) 

</div>