var new_option_;
var list_number;
var ids;
var manga_id;
var rate = 20;



console.log("Manga_details.js");

/*
*/
$(function () {
  $.ajaxSetup({
    headers: {'X-CSRF-TOKEN': $('meta[name="_token"]').attr('content')}
  });
});

$(".add_fav").submit(function (e) {
  // preventing from page reload and default actions
  e.preventDefault();
  // serialize the data for sending the form data.
  var serializedData = $(this).serialize();

  t = $(this);
  btn = t.children("button");

  // make POST ajax call
  if (btn.hasClass('btn-primary')) {
    console.log("primary")
    $.ajax({
      type: 'POST',
      url: "{% url 'main:add-to-fav' %}",
      data: serializedData,
      success: function (response) {
        // on successfull creating object

        t.children("button").removeClass("btn-primary");
        t.children("button").addClass("btn-danger");
        t.children("button").text("Unfollow");
        t.removeClass("add_to_fav");
        t.addClass("remove_from_fav");
      },
      error: function (response) {
        // alert the error if any error occured
        alert(response["responseJSON"]["error"]);
      }
    })
  } else if (btn.hasClass('btn-danger')) {
    $.ajax({
      type: 'POST',
      url: "{% url 'main:remove-from-fav' %}",
      data: serializedData,
      success: function (response) {
        // on successfull creating object

        t.children("button").removeClass("btn-danger");
        t.children("button").addClass("btn-primary");
        t.children("button").text("Follow");
        t.removeClass("remove_from_fav")
        t.addClass("add_to_fav")

      },
      error: function (response) {
        // alert the error if any error occured
        alert(response["responseJSON"]["error"]);
      }
    })
  }
})


// $(".add_to_list").submit(function (e) {
//   // preventing from page reload and default actions
//   e.preventDefault();
//   // serialize the data for sending the form data.
//   var serializedData = $(this).serialize();
//
//   t = $(this);
//   btn = t.children("button");
//
//   // make POST ajax call
//   if (btn.text().trim() == '+') {
//     $.ajax({
//       type: 'POST',
//       url: "{% url 'main:add-to-list' %}",
//       data: serializedData,
//       success: function (response) {
//         // on successfull creating object
//
//         t.children("button").text("-");
//         new_ = null
//         list_num = t.children("select").find(":selected").attr("class");
//         window.list_number[list_num - 1].push(new_)
//         console.log(window.list_number)
//       },
//       error: function (response) {
//         // alert the error if any error occured
//         alert(response["responseJSON"]["error"]);
//       }
//     })
//   } else if (btn.text().trim() == '-') {
//     console.log("primary")
//     $.ajax({
//       type: 'POST',
//       url: "{% url 'main:remove-from-list' %}",
//       data: serializedData,
//       success: function (response) {
//         // on successfull creating object
//         t.children("button").text("+");
//
//       },
//       error: function (response) {
//         // alert the error if any error occured
//         alert(response["responseJSON"]["error"]);
//       }
//     })
//   }
// })
//
//
// $('#lista').change(function () {
//   list = $(this).val()
//   val = $(this).find(":selected").val()
//   if (val == 'add new list') {
//     $('#new_option').removeClass('d-none')
//     $('#new_option_form').removeClass('d-none')
//     $('.container').css('opacity', '0.01');
//
//   }
//   class_ = $(this).find(":selected").attr("class");
//   ids = list_number[class_ - 1];
//   manga_id = null
//   console.log(ids);
//
//   if (jQuery.inArray(manga_id, ids) !== -1) {
//     $('#add_list_button').text('-')
//   } else {
//     $('#add_list_button').text('+')
//   }
//
// });
//
// $('#new_option_form').click(function () {
//   $('#new_option').addClass('d-none')
//   $('#new_option_form').addClass('d-none')
//   $('.container').css('opacity', '1');
//   $('#lista option').eq(0).prop('selected', true);
// });
//
// function myFunction() {
//   var dots = document.getElementById("dots");
//   var moreText = document.getElementById("more");
//   var btnText = document.getElementById("myBtn");
//
//   if (dots.style.display === "none") {
//     dots.style.display = "inline";
//     btnText.innerHTML = "Read more";
//     moreText.style.display = "none";
//   } else {
//     dots.style.display = "none";
//     btnText.innerHTML = "Read less";
//     moreText.style.display = "inline";
//   }
// }
//
//
// $("#new_option").submit(function (e) {
//   // preventing from page reload and default actions
//   console.log("primary");
//   e.preventDefault();
//   // serialize the data for sending the form data.
//   list_name = $(this).children("#new_option_input").val()
//   var serializedData = $(this).serialize();
//
//   t = $(this);
//   btn = t.children("button");
//
//   // make POST ajax call
//   $.ajax({
//     type: 'POST',
//     url: "{% url 'main:add-new-list' %}",
//     data: serializedData,
//     dataType: "json",
//     success: function (response) {
//       // on successfull creating object
//       $('#new_option').addClass('d-none')
//       $('#new_option_form').addClass('d-none')
//       $('.container').css('opacity', '1');
//       $('#lista option').eq(-1).prop('selected', true);
//       //===========
//       $('#option_add').before('<option>' + list_name + '</option>');
//     },
//     error: function (response) {
//       // alert the error if any error occured
//       alert(response["responseJSON"]["error"]);
//     }
//   })
// })
//
// $("#review").submit(function (e) {
//   e.preventDefault();
//   var serializedData = $(this).serialize() + "&rate=" + rate;
//   var content = $(this).children("textarea#id_content").val();
//   var username = '{{ request.user.username }}'
//   console.log(serializedData);
//   $.ajax({
//     type: 'POST',
//     url: "{% url 'main:submit-review' %}",
//     data: serializedData,
//     dataType: "json",
//     success: function (response) {
//       reviewSubmited();
//       console.log("review submited successfully");
//       $(".all_review").prepend('<div class="card mb-3"><div class="card-header">' + username.toString() + '<button class="btn btn-danger float-end">Delete</button></div><div class="card-body"><span>' + username + ' gives it ' + rate + ' Star</span><p class="card-text">' + content.toString() + '</p></div></div>');
//     },
//
//   })
//
// })


/* STAR RATE JS */
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
        <input type="text" placeholder="new list">
        <button class="btn btn-primary">Add</button>
        <a class="btn btn-danger cancel-change">cancel</a>
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
    .on('click', '#add-new-list', function (e) {
      console.log("add-new-list clicked");
    })
    .on('submit', '#add_to_list', function (e) {
      console.log('add_to_list submited');
      e.preventDefault();
      manga_id = $(this).data('manga');
      $select = $(this).find('select[name="list_name"]');
      list = $select.val();
      if (list === "new list"){
        console.log("render form to create new list");
        mangaDOM.renderListForm($(this));
      }
      else {
        console.log("add to list");
        $.ajax({
          type: 'POST',
          url: "/add_to_list/",
          data: {
            'list_name': list,
            'manga_id': manga_id,
          },
          dataType: "json",
          success: function (response) {
            console.log("added to list");
            // $('#add_to_list').addClass('d-none');
            // $('#add_to_list_form').addClass('d-none');
            // $('.container').css('opacity', '1');
            // $('#lista option').eq(-1).prop('selected', true);
            // //===========
            // $('#option_add').before('<option>' + list + '</option>');
          },
          error: function (response) {
            // alert the error if any error occured
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
