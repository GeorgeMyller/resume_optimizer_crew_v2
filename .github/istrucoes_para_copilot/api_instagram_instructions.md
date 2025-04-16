# Instruções da API do Instagram

Este documento resume como usar a API do Instagram para começar, publicar conteúdo e gerenciar menções, utilizando tanto o Login do Instagram quanto o Login do Facebook.

## Visão Geral

A Plataforma Instagram permite que aplicativos interajam com contas Profissionais do Instagram (Negócios e Criadores). Existem duas APIs principais abordadas aqui:

1.  **API do Instagram com Login do Instagram:** Usada principalmente quando o usuário do aplicativo *é* o proprietário da conta do Instagram Profissional. Requer um token de acesso do usuário do Instagram.
2.  **API do Instagram com Login do Facebook:** Usada quando o usuário do aplicativo gerencia uma Página do Facebook conectada a uma conta do Instagram Profissional. Requer um token de acesso do usuário do Facebook com permissões específicas.

## Primeiros Passos

### Pré-requisitos Comuns

*   Uma conta Profissional do Instagram (Negócios ou Criador).
*   Uma conta de Desenvolvedor do Facebook.
*   Um aplicativo registrado no Facebook (tipo Negócios é recomendado/necessário para algumas funcionalidades).

### Usando o Login do Facebook

1.  **Configurar Login do Facebook para Negócios:** Adicione o produto "Login do Facebook" ao seu aplicativo no Painel de Aplicativos.
2.  **Implementar Login:** Siga a documentação do [Login do Facebook para Negócios](https://developers.facebook.com/docs/facebook-login-for-business). Solicite as permissões `instagram_basic` e `pages_show_list`.
3.  **Obter Token de Acesso do Usuário:** Após o login bem-sucedido, capture o token de acesso do usuário do Facebook retornado.
4.  **Obter Páginas do Usuário:** Use o endpoint `GET /me/accounts` com o token de acesso para listar as Páginas do Facebook que o usuário gerencia. Capture o ID da Página conectada à conta do Instagram desejada.
5.  **Obter Conta do Instagram Business:** Use o endpoint `GET /{page-id}?fields=instagram_business_account` com o ID da Página para obter o ID do Usuário do Instagram (`ig-user-id`) conectado.
6.  **Obter Mídia (Opcional):** Use o endpoint `GET /{ig-user-id}/media` para buscar objetos de mídia da conta.

### Usando o Login do Instagram

1.  **Configurar App:** Certifique-se de que seu aplicativo Meta seja do tipo Negócios.
2.  **Obter Token de Acesso:**
    *   **Fluxo de Login:** Implemente o [Business Login for Instagram](https://developers.facebook.com/docs/instagram/platform/instagram-api/business-login). O token será de curta duração (1 hora).
    *   **Painel de Aplicativos:** Gere um token na seção "API setup with Instagram business login". O token será de longa duração (60 dias). [Estenda a validade se necessário](https://developers.facebook.com/docs/instagram/platform/instagram-api/business-login#get-a-long-lived-access-token).
3.  **Obter ID e Nome de Usuário:** Use o endpoint `GET /me?fields=user_id,username` com o token de acesso para obter o ID (`<IG_ID>`) e o nome de usuário da conta do Instagram.
4.  **Obter Mídia (Opcional):** Use o endpoint `GET /<IG_ID>/media` para buscar objetos de mídia da conta.

## Publicação de Conteúdo

Permite publicar fotos, vídeos, carrosséis, reels e stories em contas Profissionais do Instagram.

### Requisitos

*   **Permissões:** `instagram_content_publish` (e outras dependendo da ação, como `pages_read_engagement` para Login do Facebook).
*   **Token de Acesso:** Token de acesso do usuário apropriado (Instagram ou Facebook) com as permissões necessárias.
*   **Servidor Público:** A mídia a ser publicada deve estar hospedada em um URL acessível publicamente.
*   **Limite de Taxa:** 50 publicações via API por conta em um período de 24 horas. Verifique o uso com `GET /{ig-user-id}/content_publishing_limit`.
*   **Endpoints Principais:**
    *   `POST /{ig-user-id}/media`: Criar contêiner de mídia.
    *   `POST /{ig-user-id}/media_publish`: Publicar contêiner.
    *   `GET /{ig-container-id}?fields=status_code`: Verificar status da publicação (útil para vídeos).

### Fluxo de Publicação (Mídia Única - Imagem/Vídeo)

1.  **Criar Contêiner:** Envie uma solicitação `POST` para `/{ig-user-id}/media` com `image_url` ou `video_url` (e opcionalmente `caption`, `user_tags`, etc.). Para vídeos, considere o [protocolo de carregamento retomável](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-facebook-login/content-publishing#protocolo-de-carregamento-retom-vel). Para Stories, adicione `media_type=STORIES`. Para Reels, adicione `media_type=REELS` e `video_url`.
    *   *Resposta:* ID do contêiner (`<IG_CONTAINER_ID>`).
2.  **Publicar Contêiner:** Envie uma solicitação `POST` para `/{ig-user-id}/media_publish` com `creation_id` definido como o `<IG_CONTAINER_ID>` obtido na etapa 1.
    *   *Resposta:* ID da mídia publicada (`<IG_MEDIA_ID>`).

### Fluxo de Publicação (Carrossel)

1.  **Criar Contêineres de Item:** Para *cada* imagem ou vídeo no carrossel, envie `POST` para `/{ig-user-id}/media` com `image_url` ou `video_url` e o parâmetro `is_carousel_item=true`. Guarde cada ID de contêiner retornado.
2.  **Criar Contêiner de Carrossel:** Envie `POST` para `/{ig-user-id}/media` com `media_type=CAROUSEL` e o parâmetro `children` definido como uma lista separada por vírgulas dos IDs dos contêineres de item da etapa 1. Você também pode adicionar `caption`, etc.
    *   *Resposta:* ID do contêiner do carrossel.
3.  **Publicar Contêiner de Carrossel:** Envie `POST` para `/{ig-user-id}/media_publish` com `creation_id` definido como o ID do contêiner do carrossel da etapa 2.
    *   *Resposta:* ID da mídia do carrossel publicada.

### Marcação de Produtos

É possível marcar produtos em publicações únicas e carrosséis. Consulte o guia de [Marcação de Produto](https://developers.facebook.com/docs/instagram-api/guides/product-tagging).

### Solução de Problemas

*   Se a publicação de vídeo falhar ou demorar, verifique o status com `GET /{ig-container-id}?fields=status_code`. Status possíveis: `EXPIRED`, `ERROR`, `FINISHED`, `IN_PROGRESS`, `PUBLISHED`.

## Menções e Tags

Permite identificar e responder a @menções em legendas e comentários, e obter mídias onde a conta foi marcada.

### Requisitos

*   **Permissões:** `instagram_manage_comments` (para responder) e `instagram_basic`.
*   **Token de Acesso:** Apropriado com as permissões.
*   **Endpoints:**
    *   `GET /{ig-user-id}/tags`: Obter mídias onde o usuário foi marcado.
    *   `POST /{ig-user-id}/mentions`: Responder a uma @menção em um comentário ou legenda (requer `comment_id` e `message`).

### Limitações

*   Não suporta menções em Stories.
*   Não suporta comentar em fotos onde você foi marcado (use a API de Comentários padrão).
*   Webhooks para menções não funcionam se a mídia original for de uma conta privada.

### Fluxo Comum

1.  **Ouvir Webhooks (Recomendado):** Configure [Webhooks](https://developers.facebook.com/docs/instagram-platform/webhooks) para o tópico `mentions` para ser notificado sobre novas menções em comentários/legendas.
2.  **Obter Detalhes (Opcional):** Use o `comment_id` ou `media_id` do webhook para buscar mais detalhes sobre o comentário/mídia, se necessário.
3.  **Responder:** Use `POST /{ig-user-id}/mentions` com o `comment_id` da menção e a `message` da sua resposta.

## Links de Referência

*   **API com Login do Facebook:**
    *   [Get Started](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-facebook-login/get-started)
    *   [Content Publishing](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-facebook-login/content-publishing)
    *   [Mentions](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-facebook-login/mentions)
*   **API com Login do Instagram:**
    *   [Get Started](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/get-started)
    *   [Content Publishing](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/content-publishing)
    *   [Mentions](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/mentions)
*   [Referência Geral da API](https://developers.facebook.com/docs/instagram-platform/reference)
*   [Visão Geral da Plataforma](https://developers.facebook.com/docs/instagram-platform/overview)
