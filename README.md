Para correr docker promtail con loki

docker run --name promtail --volume "$PWD/promtail:/etc/promtail" --volume "/var/log:/var/log" grafana/promtail:latest -config.file=/etc/promtail/config.yaml
