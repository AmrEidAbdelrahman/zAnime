let list_id = null;
let name_div = null;
let new_name = null;

const DOM = {
  "cancel_changes": function ($element){
    console.log('cancel-changes');
    $this = $element;
    $li = $this.closest('li');
    old_name = $this.closest('div').data('original');
    console.log(old_name);
    $li.html(`
            <div class="d-block  fs-3 col-8">
                <a href="/lists/${name}/" class="mb-2">${name}</a>
            </div>
            <div class="col-2">
                <button class="btn btn-info d-inline col edit_list" >Edit</button>
            </div>
            <div class="col-2">
                <button class="btn btn-danger d-inline col delete_list">Delete</button>
            </div>`)
  },
}

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
$(function () {
  $.ajaxSetup({
    headers: {'X-CSRF-TOKEN': $('meta[name="_token"]').attr('content')}
  });
});

$(document)
    .on('click', '.edit_list', function (e) {
      console.log("edit_list clicked");
      let $li = $(this).closest('li');
      name = $li.data('name');
      console.log($li);
      $li.html(`
        <div data-original="${name}" d-flex>
          <form>
            <input type="text" name="new_name" class="form-control" value="${name}">
            <button class="btn btn-primary rounded confirm-edit">
                <span class="matrial-icons">done</span>
            </button>
            <button class="btn btn-danger rounded cancel-change">
                <span class="matrial-icons">close</span>
            </button>
          </form>
        </div>
      `)
    })
    .on('click', '.cancel-change', function (e) {
      DOM.cancel_changes($(this));
    })
    .on('click', '.delete_list', function (e) {
      console.log("delete_list clicked");
      $li = $(this).closest('li');
      name = $li.data('name');
      console.log($li);
      $li.html(`
        <div data-original="${name}">
          <p>Confirm To Delete This List.</p>
          <button class="btn btn-primary rounded confirm-edit">
              <span class="matrial-icons">done</span>
          </button>
          <button class="btn btn-danger rounded cancel-change">
              <span class="matrial-icons">close</span>
          </button>
        </div>
      `)
    })
    .on('click', '.confirm-edit', function (e) {
      console.log('confirm-edit');
      e.preventDefault();
      $form = $(this).closest('form');
      new_name = $form.find('input[name="new_name"]').val();
      list_id = $form.closest('li').data('id');
      //  send();
      let data = {
        name: new_name,
      }
      $.ajax({
        url: `/lists/${list_id}/update/`,
        type: 'POST',
        headers: {
          'X-CSRFToken': csrftoken,
        },
        data: data,
        success: function (data) {
          console.log("SUCCESS UPDATED", data);
          console.log($li);
          $li.find('a').text(new_name);
        },
        error: function (data) {
          console.log("ERROR UPDATED", data);
        }
      })
      DOM.cancel_changes($(this));
    })