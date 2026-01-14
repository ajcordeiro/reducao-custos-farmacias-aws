# 📄 Relatório de Implementação de Serviços AWS  
**Projeto: Redução de Custos em Farmácias SaúdeTotal**  
**Data:** 13/01/2026  
**Responsável:** Jaqueson Cordeiro Alves  

---

## Introdução
Este relatório apresenta o processo de implementação de soluções AWS na rede de farmácias **SaúdeTotal**, com o objetivo de reduzir custos operacionais, aumentar a escalabilidade e otimizar a gestão de dados.  

A iniciativa foi dividida em três etapas principais, cada uma focada em um serviço AWS estratégico para atender às necessidades da empresa.

---

## Etapa 1 – Amazon RDS com Auto Scaling
- **Nome da ferramenta:** Amazon RDS (Relational Database Service)  
- **Foco da ferramenta:** Banco de dados gerenciado para substituir servidores locais  
- **Descrição de caso de uso:**  
  - Migração dos bancos de dados SQL Server locais para instância RDS Multi-AZ  
  - Réplicas de leitura automáticas para lidar com picos de demanda  
  - Backup automatizado e recuperação de desastres integrada  
  - **Redução de custos:** Eliminação de licenças SQL Server e hardware local  

---

## Etapa 2 – AWS Lambda + Amazon Textract + Amazon S3
- **Nome da ferramenta:** AWS Lambda + Amazon Textract + Amazon S3  
- **Foco da ferramenta:** Automação do processamento de receitas médicas digitais  
- **Descrição de caso de uso:**  
  - Pipeline: Upload da receita → S3 → Lambda → Textract → Validação → Sistema de dispensação  
  - Substituição do processo manual de digitação de receitas  
  - **Redução de custos:** Eliminação de cargos de digitadores e ganho de eficiência (10 min → 30 seg por receita)  

---

## Etapa 3 – Amazon QuickSight
- **Nome da ferramenta:** Amazon QuickSight  
- **Foco da ferramenta:** Business Intelligence e dashboards em tempo real  
- **Descrição de caso de uso:**  
  - Substituição de relatórios manuais em Excel  
  - Conexão direta com RDS para análise de estoque, vendas e margens  
  - Alertas automáticos para reposição de medicamentos  
  - **Redução de custos:** Otimização de 30% no estoque imobilizado  

---

## Conclusão
A implementação dos serviços AWS resultou em uma redução de custos operacionais de aproximadamente **R$ 1.450.000 no primeiro ano**, além de benefícios como:  
- Escalabilidade automática para períodos sazonais  
- Maior segurança com criptografia e backups automatizados  
- Disponibilidade 24/7 para sistemas críticos  
- Insights em tempo real para tomada de decisão  

Recomenda-se a expansão futura com **Amazon Forecast**, **Amazon SageMaker** e **AWS Backup** para ampliar ainda mais os ganhos.

---

## Anexos
- Diagrama de Arquitetura AWS  
- Planilha de ROI Detalhado  
- Políticas de Segurança Implementadas  
- Manual de Operações AWS  

---

**Assinatura do Responsável pelo Projeto:**  
Jaqueson Cordeiro Alves
