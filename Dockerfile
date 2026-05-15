FROM odoo:17

# Copiamos la configuración
COPY ./config /etc/odoo

# Copiamos la carpeta con nuestros módulos personalizados a la nube
COPY ./custom_addons /mnt/extra-addons

# Arrancamos Odoo indicando que lea tanto sus módulos base como los nuestros (/mnt/extra-addons)
CMD ["sh", "-c", "exec odoo --db_host=$HOST --db_port=$PORT_DB --db_user=$USER_DB --db_password=$PASSWORD_DB --db_sslmode=require --addons-path=/mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons --http-port=$PORT"]