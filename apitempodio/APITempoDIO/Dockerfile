# ----------------------------------------------------
# Estágio 1: Build (Construção)
# Usa o SDK completo do .NET para compilar o código
# ----------------------------------------------------
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Copia o arquivo de projeto e restaura as dependências (otimização de cache)
COPY ["APITempoDIO.csproj", "."] 
RUN dotnet restore "APITempoDIO.csproj"

# Copia o restante do código-fonte e compila
COPY . .
RUN dotnet publish "APITempoDIO.csproj" -c Release -o /app/publish

# ----------------------------------------------------
# Estágio 2: Final (Runtime de Produção)
# Usa apenas o ambiente de execução e as configurações corretas
# ----------------------------------------------------
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final
WORKDIR /app
EXPOSE 8080

# CONFIGURAÇÃO CRUCIAL:
# 1. Garante que o Kestrel escute em todas as interfaces (necessário para o Docker)
# 2. Ativa o ambiente de Desenvolvimento (necessário para o Swagger UI)
ENV ASPNETCORE_URLS=http://+:8080
ENV DOTNET_ENVIRONMENT=Development

# Copia APENAS os arquivos publicados do estágio 'build'
COPY --from=build /app/publish .

# Define o comando que será executado ao iniciar o contêiner
ENTRYPOINT ["dotnet", "APITempoDIO.dll"]