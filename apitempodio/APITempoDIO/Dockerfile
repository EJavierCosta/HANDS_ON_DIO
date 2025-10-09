# ----------------------------------------------------
# Estágio 1: Build (Construção)
# ----------------------------------------------------
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Copia o arquivo de projeto e restaura as dependências
COPY ["APITempoDIO.csproj", "."] 
RUN dotnet restore "APITempoDIO.csproj"

# Copia o restante do código-fonte e compila
COPY . .
RUN dotnet publish "APITempoDIO.csproj" -c Release -o /app/publish

# ----------------------------------------------------
# Estágio 2: Final (Runtime de Produção) - USA APENAS A PORTA 80
# ----------------------------------------------------
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final
WORKDIR /app

# CONFIGURAÇÃO DE PORTA ÚNICA E CORRETA PARA AZURE APP SERVICE:
# O Azure App Service espera que a porta de exposição seja a 80
EXPOSE 80
ENV ASPNETCORE_URLS=http://+:80
ENV DOTNET_ENVIRONMENT=Development

# Copia APENAS os arquivos publicados do estágio 'build'
COPY --from=build /app/publish .

# Define o comando que será executado ao iniciar o contêiner
ENTRYPOINT ["dotnet", "APITempoDIO.dll"]