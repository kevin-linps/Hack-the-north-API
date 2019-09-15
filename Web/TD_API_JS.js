var myInit = {
    method: 'GET',
    headers: {
      'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiMDJkZTU0ZDQtY2ZkOC0zNGFkLThiNWYtYzZjODkwZDdjOTc5IiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiI3ZjIwMDMyNy0xMjE1LTQ3NmUtODEwNy1jOWQzMmE3MGQ1M2QifQ.XsJpJCXbibxFPcS98rdsKa5mQFT4uK8XUwtZMycF_e8'
    }
  };
  
  var myRequest = new Request('https://api.td-davinci.com/api/customers/90f54a9f-9112-451b-b2f9-e5de6b16e0b0', myInit);
  
  function myTdApiFunc() {
  return fetch(myRequest)
    .then(response => response.json())
    .then(json => json);
}



var uluru = {lat: json.result.addresses.principalResidence.latitude, lng: json.result.addresses.principalResidence.longitude};