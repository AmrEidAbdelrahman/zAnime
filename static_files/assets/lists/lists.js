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
                <a href="#" class="mb-2">${name}</a>
            </div>
            <div class="col-2">
                <button class="btn btn-info d-inline col edit_list" >Edit</button>
            </div>
            <div class="col-2">
                <button class="btn btn-danger d-inline col delete_list">Delete</button>
            </div>`)
  },
}

$(document)
    .on('click', '.edit_list', function (e) {
      console.log("edit_list clicked");
      $li = $(this).closest('li');
      name = $li.data('name');
      console.log($li);
      $li.html(`
        <div data-original="${name}">
          <form>
            <input type="text" name="new_name" value="${name}">
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
      //  send();
      DOM.cancel_changes($(this));
    })