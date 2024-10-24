function vote_unique_post(element) {
    const action = element.dataset.action;
    const post_id = element.dataset.id;
    const button_type = element.dataset.buttontype;
    csrfToken = document.getElementById('csrf_token').value
    console.log(element)
    console.log(action, post_id, button_type, csrfToken)

    if (action === "upvote") {
        element.setAttribute("data-action", "none");
        element.style.backgroundColor = "";
    } else if (action === "downvote") {
        element.setAttribute("data-action", "none");
        element.style.backgroundColor = "";
    } else if (action === "none" && button_type === "upvote") {
        element.setAttribute("data-action", "upvote");
        element.style.backgroundColor = "green";
    } else if (action === "none" && button_type === "downvote") {
        element.setAttribute("data-action", "downvote");
        element.style.backgroundColor = "red";
    }

    var xhr = new XMLHttpRequest();
    xhr.open('POST', post_id, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', csrfToken);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            document.querySelector('.total_votes').innerHTML = response.new_vote_total;
            if (response.new_vote === 'upvote') {
                console.log('up vote')
                document.querySelector('.upvote_btn').style.backgroundColor = "green";
                document.querySelector('.downvote_btn').style.backgroundColor = "";
            } else if (response.new_vote === 'downvote') {
                document.querySelector('.downvote_btn').style.backgroundColor = "red";
                document.querySelector('.upvote_btn').style.backgroundColor = "";
            } else if (response.new_vote === 'none') {
                document.querySelector('.downvote_btn').style.backgroundColor = "";
                document.querySelector('.upvote_btn').style.backgroundColor = "";
            }
        }
    };

    var data = JSON.stringify({ post_id: post_id, action: action, button_type: button_type, csrfToken: csrfToken });
        xhr.send(data);
}

// function sendVote(voteOption, post_id) {
//     console.log("id:", post_id, "option", voteOption)
//     var csrfToken = document.getElementById('csrf_token').value;

//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '', true);
//     xhr.setRequestHeader('Content-Type', 'application/json');
//     xhr.setRequestHeader('X-CSRFToken', csrfToken);

//     xhr.onreadystatechange = function () {
//         if (xhr.readyState === 4 && xhr.status === 200) {
//             var response = JSON.parse(xhr.responseText);
//             document.querySelector('#total_votes_' + post_id).innerHTML = response.new_vote_total;
//             if (response.new_vote === 'upvote') {
//                 document.querySelector('.upvote_btn_' + post_id).style.backgroundColor = "green";
//                 document.querySelector('.downvote_btn_' + post_id).style.backgroundColor = "";
//             } else if (response.new_vote === 'downvote') {
//                 document.querySelector('.downvote_btn_' + post_id).style.backgroundColor = "red";
//                 document.querySelector('.upvote_btn_' + post_id).style.backgroundColor = "";
//             }
//         }
//     };

//     var data = JSON.stringify({ vote: post_id, vote_option: voteOption, csrfToken: csrfToken });
//     console.log(data)
//     xhr.send(data);
// }
