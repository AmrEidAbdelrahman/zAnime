var rate = 20;



console.log("Manga_details.js");

$(function () {
  $.ajaxSetup({
    headers: {'X-CSRF-TOKEN': $('meta[name="_token"]').attr('content')}
  });
});




function reviewSubmited() {
  const btn = document.querySelector(".submit-rating");
  const thanksmsg = document.querySelector(".thanks-msg");
  const starRating = document.querySelector(".star-input");
  // Success msg show/hide
  starRating.style.display = "none";
  thanksmsg.style.display = "table";
  return false;
}

function setRate(value_) {
  rate = value_;
  displayRate();
}

function displayRate() {
  console.log(rate);
}

const mangaDOM = {
  'renderListForm': function (element) {
    console.log("renderListForm");
    element.addClass('d-none');
    $div = element.parent();
    $div.append(`
      <form id="create-new-list">
        <input type="text" placeholder="new list" name="list_name" class="form-control">
        <button class="btn btn-primary">Add</button>
        <button class="btn btn-danger cancel-change">cancel</button>
      </from>
    `)

  },
  "cancel_changes": function (element){
    console.log('cancel-changes');
    $form = element;
    $form.siblings('form').removeClass('d-none');
    $form.remove();
  },
}

$(document)
    .on('submit', '#add_to_list', function (e) {
      console.log('add_to_list submited');
      e.preventDefault();
      $select = $(this).find('select[name="list_name"]');
      list_id = $select.val();
      list = $select.val();
      if (list === "new list"){
        console.log("render form to create new list");
        mangaDOM.renderListForm($(this));
      }
      else {
        console.log("add to list");
        $.ajax({
          type: 'GET',
          url: `toggle_to_list/${list_id}/`,
          success: function (response) {
            console.log("added to list");
            $button = $select.closest('form').find('#add_list_button');
            txt = $button.text()
            txt === '+' ? $button.text('-') : $button.text('+')
          },
          error: function (response) {
            alert(response["responseJSON"]["error"]);
          }
        })
      }
    })
    .on('submit', '#create-new-list', function (e) {
      console.log("create-new-list submited");
      e.preventDefault();
      // TODO: send ajax request to create the list
      // TODO: redisplay the list options with options updated
      // TODO: change the button to remove to recognize that the manga already inserted to the list
      $form = $(this);
      $.ajax({
        type: 'POST',
        url: '/lists/add_new_list/',
        data: {
          'X-CSRFToken': $('meta[name="csrf-token"]').attr('content'),
          'list_name': $form.find('input[name="list_name"]').val(),
        },
        success: function (response) {
          console.log("list created");
          $form.siblings('form').removeClass('d-none');
          $form.remove();
          $select = $form.siblings('form').find('select[name="list_name"]');
          $select.append(`<option value="${response.id}">${response.list_name}</option>`);
          $select.val(response.id);
        },
        error: function (response) {
          alert(response["responseJSON"]["error"]);
        }
      })

    })
    .on('click', '.cancel-change', function (e) {
      mangaDOM.cancel_changes($(this).closest('form'));
    })
    .on('click', '#follow-btn', function (e) {
      console.log("follow-btn clicked");
      $btn = $(this);
      $btn.toggleClass('btn-primary');
      $btn.toggleClass('btn-danger');
      if ($btn.hasClass('btn-primary')){
        $btn.text('Follow');
      } else {
        $btn.text('UnFollow');
      }
    })
    .on('change', 'select', function (e) {
      console.log("select changed");
      $select = $(this);
      $btn = $select.siblings('button');
      lists = $select.data('lists').slice(1,-1).split(',');
      if ($select.val() === "new list"){
        $btn.text(' + ');
      } else {
        lists.includes($select.val()) ? $btn.text(' + ') : $btn.text(' - ');
      }
      // $select = $(this);
      // $select.toggleClass('d-none');
      // $select.siblings('form').toggleClass('d-none');

    })
