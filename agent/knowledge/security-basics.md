# Fundamentos de Segurança da Informação

Contexto que a skill de Análise de Vulnerabilidades usa para avaliar riscos com vocabulário correto.

## Vulnerabilidade, ameaça e risco

- **Vulnerabilidade**: uma fraqueza em um sistema, código ou processo que pode ser explorada (ex.: uma consulta SQL que concatena entrada do usuário sem validação).
- **Ameaça**: algo ou alguém com potencial de explorar uma vulnerabilidade (ex.: um atacante automatizando tentativas de injeção de SQL).
- **Risco**: a combinação entre a probabilidade de uma ameaça explorar uma vulnerabilidade e o impacto que isso causaria.

## A tríade CIA

- **Confidencialidade**: só quem é autorizado acessa a informação.
- **Integridade**: a informação não é alterada indevidamente.
- **Disponibilidade**: o sistema continua acessível para quem precisa dele.

Toda análise deveria responder: isso compromete confidencialidade, integridade, disponibilidade — ou mais de uma?

## Boas práticas gerais

- Nunca confiar em entrada do usuário sem validação.
- Usar consultas parametrizadas em vez de concatenar strings em SQL.
- Aplicar o princípio do menor privilégio.
- Manter dependências e sistemas atualizados.
- Registrar eventos de segurança para permitir investigação.
- Revisar firewall e portas abertas; não expor serviços desnecessários.

## MITRE ATT&CK

Base de conhecimento pública de táticas e técnicas usadas por atacantes reais — um vocabulário comum entre profissionais de segurança. Exemplo útil para este repositório:

- **T1190 — Exploit Public-Facing Application**: exploração de uma aplicação exposta publicamente (como um login vulnerável a SQL Injection) para obter acesso inicial.
