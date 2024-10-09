function sendVote(voteOption) {
    console.log("voteoption", voteOption)
    var postId = document.getElementById('vote_post_id').value;
    var csrfToken = document.getElementById('csrf_token').value;

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

    var data = JSON.stringify({vote: postId, vote_option: voteOption, csrfToken: csrfToken});
    try{
        xhr.send(data);
    }
    catch(err) {
        console.log(err)
    }
}