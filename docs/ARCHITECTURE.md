# Arquitetura

## Build

O repositório contém a fonte Vite. O build valida o registro de mídia e seus hashes, prepara os seis PDFs e nove aliases, aplica a política de privacidade, gera os 18 cases e compila a homepage. Por fim, grava build.txt e build.json em dist/.

public/ é a fonte versionada de assets. O build não copia pastas do diretório pai. Nenhum backend, banco de clientes ou credencial é necessário para desenvolver ou publicar o portfólio.

## Conteúdo

src/data.js define projetos e links. src/editorial-v13.js define narrativa, papel profissional e limites. scripts/evidence-map.mjs define as galerias. As capturas dos cinco destaques em src/v8-story.json devem existir também no case correspondente. Os IDs de evidência permitem deep links entre a homepage, uma captura específica e a galeria ampliada.

templates/case.html e os renderizadores em scripts/ geram public/projetos/. Esses HTML são saída de geração fora do Git; o gerador continua sendo a fonte da mudança.

## Movimento

src/motion-preference.js resolve Automático, Animação e Leitura direta. A preferência explícita é persistida, com fallback se o armazenamento falhar. GSAP e o complemento mobile obedecem ao mesmo estado; mudanças limpam timelines e estilos incompatíveis.

Desktop mantém a narrativa dos cinco protagonistas. Celulares e telas baixas usam fluxo natural. Leitura direta oferece capturas proporcionais, miniaturas, legendas e acesso ao case. O HTML inclui links e evidências antes do JavaScript.

## Currículos e legado

scripts/resumes-content.json é a fonte editorial dos seis PDFs. A regeneração usa Python e exige inspeção visual; o build web preserva os arquivos já validados.

Os antigos /cases/, /en/ e /competencias/ continuam acessíveis, identificados como acervo e excluídos de indexação. O sitemap prioriza os cases atuais. URLs antigas de PDFs permanecem como aliases binários, fora do catálogo de seis versões.

## Verificação

Playwright testa comportamento e geometria; axe-core detecta parte das falhas de acessibilidade. A CI usa o mesmo build para teste e publicação. A conferência online compara todos os hashes do manifesto, além do commit publicado.
