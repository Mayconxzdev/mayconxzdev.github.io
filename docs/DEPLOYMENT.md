# Publicação e rollback

## Fluxo normal

1. Trabalhe em uma branch e altere as fontes.
2. Execute npm ci, npm run build e npm run test:full.
3. Se alterar PDFs, execute a verificação Python e confira as páginas renderizadas.
4. Revise o diff e a política de mídia. Abra um PR.
5. A CI valida o build do PR. Após a integração em main, publica somente dist/.
6. A etapa verify-live confere build.txt, build.json e os hashes de todos os arquivos contra o artefato testado.

O GitHub Pages precisa usar GitHub Actions como fonte de publicação. O workflow .github/workflows/pages.yml já implementa build, regressão, artifact, deploy e conferência online. Branches e PRs não fazem deploy.

## Diagnóstico

Confira a execução de Actions, o arquivo público /build.txt e /build.json. Um HTTP 200 ou um check de compilação, isoladamente, não demonstra que a versão pretendida foi publicada. Os hashes servem para identificar o artefato exato, incluindo PDFs e HTML de cases.

O manifesto também registra .nojekyll, um marcador consumido pelo GitHub Pages que não é servido por HTTP. Essa única entrada é identificada como arquivo exclusivo do artefato; todos os recursos públicos continuam sendo verificados por tamanho e SHA-256.

## Rollback

O histórico anterior à normalização está preservado no Git. O último head publicado antes desta entrega era 6e1506c870e0692c7832ce02f6cea4ce6c532357.

Para um rollback de conteúdo dentro da estrutura atual, prefira um commit de revert em uma branch, valide e integre pelo mesmo fluxo. Não faça force-push em main.

Para restaurar o formato estático anterior completo, restaure também o workflow compatível daquele commit em uma branch de rollback. Esse formato não possui a árvore Vite e não deve ser misturado parcialmente com o workflow atual. Confira os checks e os arquivos servidos depois do deploy.

Backups locais e pacotes de auditoria são preservados fora do repositório público. A autorização de mídia não é ampliada automaticamente por um rollback.
