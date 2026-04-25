# 🧠 Sistema de Controle

<div style="text-align: justify;">

O sistema de controle do MICKY segue uma arquitetura híbrida, combinando processamento de alto nível com controle embarcado de baixo nível.

Esta seção apresenta o sistema de controle de locomoção do MICKY.

---

## Comunicação

A comunicação entre o computador embarcado e o microcontrolador é realizada por meio de uma interface serial.

Os comandos de velocidade são transmitidos utilizando o seguinte formato:

```text
<v_x, v_y, ω>
```

Esse protocolo leve garante comunicação de baixa latência entre os sistemas de alto e baixo nível.

---

## Firmware do Microcontrolador

O firmware do microcontrolador foi projetado para execução de baixa latência e não bloqueante.

Ele utiliza as bibliotecas `Wire.h` e `AccelStepper.h` para garantir controle eficiente dos motores e comunicação com sensores.

O loop principal de controle é composto por:

1. Recepção de comandos via serial  
2. Mecanismo de segurança (fail-safe)
3. Processamento cinemático 
4. Aquisição de sensores
5. Controle dos motores 

A telemetria inclui:

- orientação
- aceleração
- velocidade angular
- temperatura

---

## Integração com ROS 2

O sistema é integrado ao ROS 2 por meio de dois nós principais:

- **CmdVelToSerial** — converte comandos de velocidade em mensagens seriais
- **ImuSerialPublisher** — publica dados da IMU

Essa arquitetura permite integração direta com frameworks de navegação e controle de alto nível.

</div>