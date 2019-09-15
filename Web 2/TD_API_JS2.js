var myInit = {
  method: 'GET',
  headers: {
    'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiMDJkZTU0ZDQtY2ZkOC0zNGFkLThiNWYtYzZjODkwZDdjOTc5IiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiI3ZjIwMDMyNy0xMjE1LTQ3NmUtODEwNy1jOWQzMmE3MGQ1M2QifQ.XsJpJCXbibxFPcS98rdsKa5mQFT4uK8XUwtZMycF_e8'
  }
};

var myRequest = new Request('https://api.td-davinci.com/api/customers/abea2e58-13aa-4f74-8816-4da6960fe2bf', myInit);

fetch(myRequest)
  .then(response => response.json())
  .then(json => {
    
    console.log(json);
  });

