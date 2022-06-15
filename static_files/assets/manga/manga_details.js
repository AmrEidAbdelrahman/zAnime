var rate = 20;
let lists = []
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

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
            let $button = $select.closest('form').find('#add_list_button');
            console.log($button.text());
            let txt = $button.text()
            txt.trim() === '+' ? $button.text(' - ') : $button.text(' + ')
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
      let $form = $(this);
      let manga_id = $form.data('manga');
      let list_name = $form.find('input[name="list_name"]').val();
      let data = {
        'manga_id': 3,
        'list_name': list_name
      }
      console.log(JSON.stringify(data));
      $.ajax({
        type: 'POST',
        url: '/lists/add_new_list/',
        headers: {'X-CSRFToken': csrftoken},
        data: JSON.stringify(data),
        contentType:'application/json',
        success: function (response) {
          lists.push(response.list.id);
          console.log(lists);
          let $select_form = $form.siblings('form');
          $select_form.removeClass('d-none');
          let $select = $select_form.find('select');
          $select.prepend(`
            <option id="${response.list.id}" value="${response.list.id}">${list_name}</option>
          `);
          $select.val(response.list.id);
          $select_form.find(".btn").text(' - ');
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
      $.ajax({
        type: 'GET',
        url: `toggle_follow/`,
        success: function (response) {
          console.log("followed");
          if ($btn.hasClass('btn-primary')){
            $btn.text('Follow');
          } else {
            $btn.text('UnFollow');
          }
        }
      })
    })
    .on('change', 'select', function (e) {
      console.log("select changed");
      let $select = $(this);
      let $btn = $select.siblings('button');
      lists = $select.data('lists').slice(1,-1).split(', ');
      console.log(lists);
      if ($select.val() === "new list"){
        $btn.text(' + ');
      } else {
        console.log($select.val())
        console.log(lists.includes($select.val()))
        lists.includes($select.val()) ? $btn.text(' - ') : $btn.text(' + ');
      }
      // $select = $(this);
      // $select.toggleClass('d-none');
      // $select.siblings('form').toggleClass('d-none');

    })
