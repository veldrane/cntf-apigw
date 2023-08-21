- vysvetlit proc apigw potrebujeme
    - ekosystem se rozrusta => chaos
    - centralizovany management
    - bezpecnost
    - integrace stavajicich api s infrastrukturou
    - service discovery
    - rate limiting
    - integrace s idp
    - ceakce na chyby backend aplikaci/microservice (circuit breaking)
    - sprava chybovych stavu
    - vedet co publikuji za informace



- popovidat o openapi standardech, ukazat swagger a swagger ui
- moznosti na trhu - comunitni i enterprice nastroje
    - krakend
    - openresty
    - kong
    - traefik
    apod

- reverse proxy, ingress vs apigw !
    - obrazek public cast <-> logika <-> backend
        - zduraznit dulezitost logicke vrstvy v apigw proti blbe reverse proxy

- reseni pro odvazne (Openresty)

- reseni pro line :) (Krakend)

- obecna konfigurace
    - pozadavek => logika => backend => logika => odpoved

- logika
    - filtering
    - request/response data manipulation
    - response caching
    - circuit breaker
    - rate limiting
    - integrace s 3rd party sw (IdP, message brokery apod)
    - error handling

- nekde tam budem muset zminit routing sluzeb (uz jen kvuli tomu slovicku :)
. mozna se pobavit o service discovery


- produkty: OpenResty, Krakend, Kong, Tyk, Traefik, 3scale 