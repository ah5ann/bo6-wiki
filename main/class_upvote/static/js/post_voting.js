function sendVote_unique(voteOption) {
    var postId = document.getElementById('vote_post_id').value;
    var csrfToken = document.getElementById('csrf_token').value;
    console.log("ID: ", postId)

    var xhr = new XMLHttpRequest();
    xhr.open('POST', postId, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', csrfToken);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response)
            document.querySelector('.total_votes').innerHTML = response.new_vote_total;
            console.log(response)
            if (response.new_vote === 'upvote') {
                console.log('up vote')
                document.querySelector('.upvote_btn').style.backgroundColor = "green";
                document.querySelector('.downvote_btn').style.backgroundColor = "";
            } else {
                document.querySelector('.downvote_btn').style.backgroundColor = "red";
                document.querySelector('.upvote_btn').style.backgroundColor = "";
            }
        
        }
    };

    var data = JSON.stringify({ vote_option: voteOption, csrfToken: csrfToken });
        xhr.send(data);
}

function sendVote(voteOption, post_id) {
    console.log("id:", post_id, "option", voteOption)
    var csrfToken = document.getElementById('csrf_token').value;
    var vote_total_id = document.querySelector('.total_votes').id
    console.log(vote_total_id)

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', csrfToken);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            document.querySelector('#total_votes_' + post_id).innerHTML = response.new_vote_total;
            if (response.new_vote === 'upvote') {
                document.querySelector('.upvote_btn_' + post_id).style.backgroundColor = "green";
                document.querySelector('.downvote_btn_' + post_id).style.backgroundColor = "";
            } else {
                document.querySelector('.downvote_btn_' + post_id).style.backgroundColor = "red";
                document.querySelector('.upvote_btn_' + post_id).style.backgroundColor = "";
            }
        
        }
    };

    var data = JSON.stringify({ vote: post_id, vote_option: voteOption, csrfToken: csrfToken });
        xhr.send(data);
}
