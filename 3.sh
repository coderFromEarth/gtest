#!/bin/bash
if true | openssl s_client -connect ams-evo1.yusp.com:443 2>/dev/null | \
  openssl x509 -noout -checkend 2592000; then
  echo "Congratulation, your certificate is good to go!"
else
  echo "Please, replace the certificate as soon as possible!"
fi
