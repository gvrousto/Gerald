let search_results = document.getElementById("searchResults");
let searchbar = document.getElementById('searchbar');


searchbar.addEventListener('input', (e) => {
  search_results.style.display = "none";
  var searchquery = 'https://www.instagram.com/web/search/topsearch/?context=blended&query=' + searchbar.value
  var results = fetch(searchquery)
    .then(res => res.json()
    ).then((res) => {
        var ulen = res.users.Length;
        let users = []
        for (var i = 0; i < 5; i++) {
          users.push(res.users[i].user);
          console.log(res.users[i].user)
        }
        updateSearch(users);
    })
});

function updateSearch (users) {

  var result = ""
  for (var i = 0; i < users.length; i++) {
    console.log(users[i].profile_pic_url)

    result += `
      <div class="result noselect" onclick="search('${users[i].username}')")>
        <div class="result-thumb">
          <img class="thumbnail" src="${users[i].profile_pic_url}">
        </div>
        <div class="result-name">
          ${users[i].username}
        </div>
      </div>
    `;
  }
  search_results.innerHTML = result;
  search_results.style.display = "block";
}

function search(query) {
  search_results.innerHTML = ""
  searchbar.value = ""
  searchbar.placeholder = query;
  search_results.innerHTML = `
    <div>
      <img src="images/loading.svg" class="centered" style="width:120px;">
    </div>
  `
}
/*function updateSearch(e) {
  console.log(e)
  fetch('https://www.instagram.com/web/search/topsearch/?context=blended&query=' + e)
  search_results = ""
}*/
