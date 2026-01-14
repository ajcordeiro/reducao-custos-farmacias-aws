# 💊 Redução de Custos em Farmácias com AWS

Este repositório apresenta a implementação de soluções baseadas em serviços da Amazon Web Services (AWS) na rede de farmácias **SaúdeTotal**, com foco em redução de custos operacionais, automação de processos e análise de dados em tempo real.

## 📌 Objetivo

Reduzir os custos operacionais em pelo menos **30%** por meio da adoção de três serviços AWS estratégicos:

- **Amazon RDS com Auto Scaling**
- **AWS Lambda + Amazon Textract + Amazon S3**
- **Amazon QuickSight**

## 🏥 Cenário

A rede SaúdeTotal possui 50 unidades distribuídas pelo estado, enfrentando desafios como:

- Gerenciamento descentralizado de estoque  
- Processamento manual de receitas médicas  
- Falta de dashboards em tempo real para análise de vendas e reposição  

## ⚙️ Soluções Implementadas

- **Amazon RDS** → Migração de bancos locais para instância Multi-AZ com réplicas de leitura automáticas  
- **AWS Lambda + Textract + S3** → Automação do processamento de receitas médicas digitais  
- **Amazon QuickSight** → Dashboards em tempo real conectados ao RDS para análise de estoque e vendas  

## 💰 Resultados

- **Economia anual:** R$ 1.590.000  
- **Redução percentual de custos:** 41,73%  
- **ROI:** 41,73%  
- **Payback:** 1,9 meses  
- Eliminação de licenças e servidores locais  
- Redução de tempo de processamento de receitas de **10 minutos para 30 segundos**  
- Otimização de **30% no estoque imobilizado**  

## 📄 Relatório Completo

👉 [Relatório de Implementação de Serviços AWS](documentacao/relatorio-implementacao.md)

## 📎 Anexos

- [Diagrama de Arquitetura AWS](arquitetura/diagrama-aws.png)  
- [Resumo Executivo ROI (PDF)](calculos/resumo-executivo-roi-atualizado.pdf)  
- [ROI Calculator (Excel)](calculos/roi-calculator.xlsx)  
- [Dashboard ROI Corrigido (Excel)](calculos/dashboard_roi_corrigido.xlsx)  
- [TCO Analysis](calculos/tco-analysis.pdf)  
- [Política de Segurança](documentacao/politica-seguranca.md)  
- [Manual de Operações](documentacao/manual-operacoes.md)  

---


