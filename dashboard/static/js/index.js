$(document).ready(function() {

  $('.dropdown-toggle').click(function(e) {
    e.preventDefault();
    $(this).next('.dropdown-menu').toggle();
  });
  
  function submitForm() {
    var form = $("#formNovaEmpresa")[0];
    var formData = new FormData(form);
    formData.append("csrfmiddlewaretoken", "{% csrf_token %}");
    $.ajax({
        url: "{% url 'novaEmpresa' %}",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        },
        success: function(response) {
            console.log(response);
        },
        error: function(xhr, status, error) {
            console.log(xhr.responseText);
        }
    });
  }
  // function to update CNPJ data
  function updateCNPJ() {
      $.ajax({
          type: "POST",
          url: "/editarempresa/",
          data: {
              cnpj: $('#cnpjInput').val(),
              name: $('#id_name').val(),
              active: $('#inputState').val(),
              csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          },
          success: function(response) {
              if (response.success) {
                  // update the card with the new data
                  $('#cnpj-card .list-group-item p:first-child').text(response.cnpj);
                  $('#cnpj-card .list-group-item p:nth-child(2)').text(response.name);
                  $('#cnpj-card .list-group-item span').text(response.active).toggleClass('bg-success bg-dark');
                  // close the modal
                  $('#editandoCNPJ').modal('hide');
              } else {
                  // handle the error
                  alert(response.message);
              }
          },
          error: function(xhr, status, error) {
              console.log(xhr.responseText);
              // handle the error
              alert('Error updating CNPJ data.');
          }
      });
  }

  // function to add CNPJ data
  function addCNPJ() {
      $.ajax({
          type: "POST",
          url: "/editarempresa/",
          data: {
              cnpj: $('#cnpjInput').val(),
              name: $('#id_name').val(),
              active: $('#inputState').val(),
              csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          },
          success: function(response) {
              if (response.success) {
                  // add the new data to the card
                  var html = '<li class="list-group-item d-inline-flex align-items-center gap-5">' +
                      '<p class="flex-grow-1 mb-0">' + response.cnpj + '</p>' +
                      '<p class="flex-grow-1 mb-0">' + response.name + '</p>' +
                      '<span class="badge rounded-pill bg-success">' + response.active + '</span>' +
                      '<button class="btn btn-outline-primary" type="button" data-bs-toggle="modal" data-bs-target="#editandoCNPJ">' +
                      '<i class="bi bi-pencil-square"></i> Editar</button>' +
                      '</li>';
                  $('#cnpj-card .list-group').append(html);
                  // close the modal
                  $('#adicionandoCNPJ').modal('hide');
              } else {
                  // handle the error
                  alert(response.message);
              }
          },
          error: function(xhr, status, error) {
              console.log(xhr.responseText);
              // handle the error
              alert('Error adding CNPJ data.');
          }
      });
  }

  // function to display CNPJ data
  function displayCNPJ() {
      $.ajax({
          type: "GET",
          url: "/editarempresa/",
          success: function(response) {
              if (response.success) {
                  // display the CNPJ data in the card
                  $('#cnpj-card .list-group-item p:first-child').text(response.cnpj);
                  $('#cnpj-card .list-group-item p:nth-child(2)').text(response.name);
                  $('#cnpj-card .list-group-item span').text(response.active).toggleClass('bg-success bg-dark');
              } else {
                  // handle the error
                  alert(response.message);
              }
          },
          error: function(xhr, status, error) {
              console.log(xhr.responseText)
              alert('Error updating CNPJ data: ' + error);
          }
      });
  }
})
