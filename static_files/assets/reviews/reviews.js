


$(document)
  .on('submit', '#review', function (e) {
    e.preventDefault();
    console.log('review submited');
    let $form = $(this);
    let review = $form.find('textarea[id="review_text"]').val();
    let $all_reviews = $('#all_reviews');
    console.log($all_reviews);
    $.ajax({
      type: 'POST',
      headers: {
        'X-CSRFToken': csrftoken
      },
      url: `review/`,
      data: {
        'review': review,
      },
      success: function (response) {
        console.log("review added");
        $form.before(`
        <div class="thanks-msg text-left">Thanks for your feedback !!!</div>
        `)
        $all_reviews.append(`
        <div class="review-item" data-id="${response.review.id}">
            <div class="card mb-3">
                <div class="card-header">
                    ${response.review.user}
                    <button class="btn btn-danger float-end delete-review">Delete</button>
                </div>
                <div class="card-body">
                    <p class="card-text">${response.review.content}</p>
                </div>
            </div>
        </div>
        `)
        $form.remove();

      }
    })
  })
  .on('click', '.delete-review', function (e) {
    console.log('delete-review clicked');
    let $review_item = $(this).closest('.review-item');
    let review_id = $review_item.data('id');
    console.log(review_id);
    $.ajax({
      type: 'Delete',
      headers: {
        'X-CSRFToken': csrftoken
      },
      url: `/review/${review_id}/`,
      success: function (response) {
        $review_item.remove();
      }
    })
  })