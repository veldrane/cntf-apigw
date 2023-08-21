---
title: Stavime Api gateway
separator: <!--s-->
verticalSeparator: <!--v-->
transition: 'fade'
data-separator-notes: "^Notes:"
---


<!-- .slide: data-background="images/ApiGW-cntf-v1.png" data-background-size="1920px"  -->

Co API Gateway je a proč ji potřebujeme

Notes:
Uvodni Stranka
<!--s-->


<!-- .slide: data-background="images/ApiGW-cntf-v1-restapi-dnes.png" data-background-size="1920px"  -->

Notes:
- Obrazek chaosu kterej musime vytvorit
- Popis: 
  - 3 druhy REST API:
    - Api pro frontend
    - Api pro komunikaci mezi internimi aplikacemi
    - Api pro vymenu dat mezi nasi spolecnosti a 3 stranou
  - Pro kazdy druh muzeme chtit neco jineho
    - Jinou uroven zabezpeceni
    - Jiny Accounting
    - Jinou integraci s nasi infrastrukturou
<!--s-->


<!-- .slide: data-background="images/ApiGW-cntf-v1.png" data-background-size="1920px"  -->

#### REST API je dnes především zdrojem dat!

Notes:
- Popis:
  - Zduraznit zdroj dat!
  - Zdurazni zdroj strukturovanych dat
  - takovych ktere druha strana muze tridit, analyzovat a pouzit pro sve ucely
  - UVest priklad se server page stranakama kde tato data byla "zahnojena html"

<!--s-->

<!-- .slide: data-background="images/ApiGW-cntf-v1.png" data-background-size="1920px"  -->

#### Data potřebujeme

<div id=left2>

* konsolidovat
* bezpečně publikovat
* integrovat

...zkrátka mít nad nimi kontrolu!

</div>


Notes:
- <BR>
- nutne zminit ze jejich velikost roste<BR>
- (zminka) jazyk c<BR>
- integrace myšleno mezi sebou i s naší infrastrukturou
<!--s-->

<!-- .slide: data-background="images/ApiGW-cntf-v1.png" data-background-size="1920px"  -->

#### Co je Api Gateway

* Reverzní proxy která:
  * je orientována na práci s REST požadavky
  * umožnuje jejich filtering, transformace, apod.
  * integruje naše API s dalšími prvky naší infrastruktury.
  * další možné funkce: 
    * service discovery
    * rate limiting
    * circuit breaking atd


Notes:
- Popis:
  - Integrace, zminit moznost provazat api treba s ad apod
  - Service discovery, zminit moznost sd pomoci treba nejakeho jsonu

<!--s-->

<!-- .slide: data-background="images/ApiGW-cntf-v1-apigw-example.png" data-background-size="1920px"  -->

Notes:
  - Popis:
    - proste reverzni proxy :)

<!--s-->

<!-- .slide: data-background="images/ApiGW-cntf-v1.png" data-background-size="1920px"  -->

| Api Gateway                               | Reverse Proxy/Ingress                   |
| :---                                      | :---                                    |
| Zaměřena na manipulaci s rest požadavky   | Zeměření na přístup k aplikaci          |
| Mix obecné a "fine grained" konfigurace   | Obecná konfigurace                      |
| Transfomace request/response, views..     | SSL terminace, segmentace               |
| Service owner: vývoj/infrastruktura       | Service owner: infrastruktura           |


Notes:
- budem muset hodne upravit - nejsem ve forme :/

<!--s-->

<!-- .slide: data-background="images/ApiGW-cntf-v1.png" data-background-size="1920px"  -->

DYI Api Gateway

<!--s-->


<!-- .slide: data-background="images/ApiGW-cntf-v1-openresty.png" data-background-size="1920px"  -->


<!--s-->

<!-- .slide: data-background="images/ApiGW-cntf-v1.png" data-background-size="1920px"  -->

#### OpenResty (Nginx + Lua VM) - Api Gateway pro odvážné :)

<div if=left2>

* Modifikovaní flow pomocí lua skriptů
* Spousta pluginů
* Často jako základ jiných sw (Kong, ruzná CMS apod)
* Jedná se spíše o framework

</div>

<div id=resources>

[https://openresty.org/](https://openresty.org/)<BR>
[https://github.com/openresty/lua-nginx-module](https://github.com/openresty/lua-nginx-module)<BR>
[https://openresty-reference.readthedocs.io/en/latest/Directives/](https://openresty-reference.readthedocs.io/en/latest/Directives/)

</div>

Notes:
- <BR>
- flow myslime nginx flow<BR>
- zminit mozne integrace se redisem apod<BR>
- zminit performance <BR>

<!--s-->

<!-- .slide: data-background="images/ApiGW-cntf-v1.png" data-background-size="1920px"  -->

#### OpenResty - příklad konfigurace


```
location /mutex {
            set $locid 14;
            access_by_lua_block {

                -- Main
                local mutexes = ngx.shared.mutexes;
                local session_id = ngx.var.arg_id;
                local mutex, err = mutexes:get(session_id)

                if mutex == nil then
                  local ok, err, force = mutexes:add(session_id,1, 5);
                  ngx.exit(ngx.HTTP_CREATED);
                end;

                ngx.exit(ngx.HTTP_NO_CONTENT);
              }
}

```

<!--s-->

<!-- .slide: data-background="images/ApiGW-cntf-v1.png" data-background-size="1920px"  -->

#### Proč Openresty

* Je to Nginx :)
* Lua skriptování je jednoduchý ale velmi mocný nástroj
* Spousta pluginů
* Široká komunita
* Slušný výkon

<!--s-->

<!-- .slide: data-background="images/ApiGW-cntf-v1.png" data-background-size="1920px"  -->

#### Openresty - temná strana síly

* Mix infrastruktury a vývoje (nedá se tomu uplně vyhnout :) 
* Naročné na údržbu a deployment
* Některé pluginy jsou oneman show s diskutabilní podporou
* Občas složité kódování logiky (např. zavislé na response body)
  * někdy může být vhodnějši NGINX Javascript (je možné oba moduly kombinovat)

Notes:
  - Popis:
    - Mix infra a vyvoje - v tomto pripade se tomu neda moc vyhnout

<!--s-->

<!-- .slide: data-background="images/ApiGW-cntf-v1.png" data-background-size="1920px"  -->

#### Krakend

<div if=left2>

* CE je Stateless
* Napsán v golangu
* Vynikající dokumentace
* Konfigurace je v jsonu, možnost použití designeru
* Podpora pro: Filtering a transformace http requestů
  * OIDC
  * Rate Limiting
  * Circuit breaking
* Rozšiřitelný pomocí custom pluginů

</div>

<div id=resources>

[https://www.krakend.io/](https://www.krakend.io/)<BR>
[https://www.krakend.io/docs/overview/introduction/](https://www.krakend.io/docs/overview/introduction/)<BR>
[https://designer.krakend.io/](https://designer.krakend.io/#!/)
</div>

Notes:
- "Pokud je openresty reseni pro odvazne pak krakend je resenim pro line :)"
- ukazka designeru
- OIDC je podpora pouze implicitniho flow - tyka se ce edice

<!--s-->

<!-- .slide: data-background="images/ApiGW-cntf-v1.png" data-background-size="1920px"  -->

#### Krakend - příklad konfigurace


```
        {
          "endpoint": "/simple/articles",
          "method": "GET",
          "extra_config": {
              "github.com/devopsfaith/krakend-jose/validator": {
                  "alg": "RS256",
                  "roles_key": "groups",
                  "roles": ["simple-admin","simple-user"],
                  "jwk-url": "https://secure-keycloak-keycloak.route.local/auth/realms/lab/protocol/openid-connect/certs",
                  "disable_jwk_security": true
              }
           },
          "backend": [
            {
              "url_pattern": "/articles",
              "encoding": "json",
              "is_collection": true,
              "extra_config": {
                  "github.com/devopsfaith/krakend/proxy": {
                      "flatmap_filter": [
                          {
                              "type": "del",
                              "args": ["collection.*.Id"]
                          }
                      ]
                  }
              }, 
              "host": [
                "http://simpleapi.simple.svc.cluster.local:8080"
              ]
            }
```

<!--s-->



<!-- .slide: data-background="images/ApiGW-cntf-v1.png" data-background-size="1920px"  -->

#### Další projekty

* 3scale
* Kong
* Tyk
* Traefik
* Plus projekty v rámci public cloud subscripce

Notes:
- pouze vyjmenovat

<!--s-->

<!-- .slide: data-background="images/ApiGW-cntf-v1.png" data-background-size="1920px"  -->

#### Pasti, pasti, pastičky

<div id=left2>

* Bude naše apigw statefull nebo stateless ?
  * specialně pozor na nasazení v k8s
  * statefull - možný dopad na škálování
* V kubernetes některé funkce zvolené (dodané) CNI - pozor na to.
* Jak nasazení ovlivní provoz a deployment backend služeb ?
* Jedna nebo více instancí ?
* Chceme některé funkcionality přenést z aplikace na apigw ? 
  * typicky autorizace, session management apod...
* Máme dostatek lidských zdrojů na implementaci požadovaného řešení ?

</div>

Notes:
 Popis:
  - Ve statefull prostředí se pravdepodobně nevyhneme integraci s nějakým (key/val) storem (redis, memcached aj)
  - Zduraznit ze apigw jako kazda konsolodujici sluzba jde primo proti cntf principu (preformulovat)
  - Je potreba si dukladne rozmyslet dopady na sluzby z hlediska operations 
  - Lide jsou vetsion bud dobri programatori nebo dobri infra specialist, malokdy oboji.
    - Apigw je casto prunik obojiho.

<!--s-->


<!-- .slide: data-background="images/ApiGW-cntf-v1.png" data-background-size="1920px"  -->

#### Co pomůže


* V maximální míře využívat OpenAPI
  * generování konfigurace na základě swaggeru
* Rozděl a panuj!
* Méně je více

<!--s-->

<!-- .slide: data-background="images/ApiGW-cntf-v1-questions.png" data-background-size="1920px"  -->

<!--s-->