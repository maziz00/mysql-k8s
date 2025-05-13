curl -X POST http://<EC2_IP>:30080/log-ip



mysql -h <EC2_IP> -P 30306 -u api -p iplog
# Password: apipassword
SELECT * FROM ips;



kubectl port-forward -n db pod/mysql-secondary-0 3307:3306


mysql -h 127.0.0.1 -P 3307 -u api -p iplog


kubectl run mysql-client -n db --rm -it --image=mysql:8.0 -- \
  mysql -h mysql-primary.db.svc.cluster.local -u api -p iplog
# Password: apipassword