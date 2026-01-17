Invoke-WebRequest -Uri "https://graph.facebook.com/v17.0/979232561930143/messages" `
  -Method POST `
  -Headers @{Authorization = "Bearer EAAM0599SPNEBQYzS0bYsUx6VMLZB7pG7inzaZA6II7K7ZCgGbBgWYEmvfrt1KZAqZBZCT9MxZCXQHYMnUZBZBSbZAZCZCannmgGsUNIaUsTVcH5zbmIm8VnCKdHA18fnm9vr2drLN9ZBQC2mMlxlSOXPZAGqMXSI1TujMwe4KciDJqcyW5Jy3tF5JZC2fsl1QfYniRZAUNfRZBwZDZD"; "Content-Type" = "application/json"} `
  -Body '{ "messaging_product": "whatsapp", "to": "212644700110", "type": "text", "text": { "body": "Hello Soufiane, permanent token test!" } }'
