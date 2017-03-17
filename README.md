# odoo-dev-kickstart

## Para usar
1. Instalar vagrant e VirtualBox
2. Gerar uma chave ssh (ssh-keygen)
3. Importar essa chave (pública) para o github
4. Clonar esse repositório git@github.com:virgilio-bradoo/odoo-dev-kickstart.git
5. $ vagrant up
6. Tome um café

## FAQ
### VirtuaBox dá problema dizendo que o modulo do kernel não está instalado
1. Instale o módulo
2. Carregue o modulo 
3. Há um erro comum ao subir o modulo, procure sobre como assinar o modulo antes de subir
### O que devo importar no Github?
Após rodar o ssh-keygem, vão ser criados (se já não existirem) dois arquivos num diretório .ssh dentro da raiz do seu home, pegue o conteúdo do arquivo .pub =) O nome padrão é id_rsa.pub

