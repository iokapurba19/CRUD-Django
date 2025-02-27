function changeCardStyle(card, isHover) {
    const icon = card.querySelector('.card-icon');
    if (isHover) {
      card.style.backgroundColor = 'rgba(0, 123, 255, 0.8)'; // Warna biru lembut
      card.style.color = 'white'; // Ubah warna teks menjadi putih saat hover
      icon.style.color = 'white'; // Ubah warna ikon menjadi putih saat hover
    } else {
      card.style.backgroundColor = 'white'; // Kembali ke latar belakang putih
      card.style.color = '#343a40'; // Kembali ke warna teks default
      icon.style.color = '#007bff'; // Kembali ke warna ikon default
    }
}
$(function () {
  // Aktifkan tab pertama secara default
  $('.nav-pills a:first').tab('show');

  // Tambahkan event listener untuk tab
  $('.nav-pills a').on('click', function (e) {
      e.preventDefault();
      $(this).tab('show');
  });
});

function showImage(imageUrl, title) {
  // Show loading spinner
  $('#imageLoader').show();
  $('#modalImage').css('opacity', '0');

  // Update modal content
  $('#modalImage').attr('src', imageUrl);
  $('#imageModalLabel').text(title);
  $('#downloadBtn').attr('href', imageUrl);

  // Hide spinner and show image when loaded
  $('#modalImage').on('load', function() {
      $('#imageLoader').hide();
      $(this).css('opacity', '1');
  });

  // Show modal
  $('#imageModal').modal('show');
}

// Handle keyboard events
$(document).keyup(function(e) {
  if (e.key === "Escape") {
      $('#imageModal').modal('hide');
  }
});

// Prevent right click on images
$('.img-preview').on('contextmenu', function(e) {
  return false;
});

// Reset modal on close
$('#imageModal').on('hidden.bs.modal', function () {
  $('#modalImage').attr('src', '');
  $('#imageLoader').show();
});

// Handle modal loading state
$('#imageModal').on('show.bs.modal', function () {
  $('#modalImage').css('opacity', '0');
  $('#imageLoader').show();
});

$(document).ready(function () {
    $('.only-numbers').on('input', function () {
        console.log("Input detected: ", this.value); // Debugging log
        // Hapus semua karakter selain angka
        this.value = this.value.replace(/[^0-9]/g, '');
    });
});


/**
   * Fungsi untuk memformat input currency dengan jQuery
   * @param {string} elementId - ID elemen input yang akan diformat
   */
  function initializeCurrencyFormatter(elementId) {
    const $inputElement = $(`#${elementId}`); // Menggunakan jQuery untuk seleksi elemen

    if ($inputElement.length === 0) {
      console.error(`Element with ID "${elementId}" not found.`);
      return;
    }

    $inputElement.on('input', function () {
      let value = $(this).val().replace(/[^0-9]/g, ''); // Hapus karakter selain angka
      $(this).val(formatRupiah(value));
    });
  }

  /**
   * Fungsi untuk memformat angka menjadi format Rupiah
   * @param {string} angka - String angka yang akan diformat
   * @returns {string} - Angka yang diformat dalam format Rupiah
   */
  function formatRupiah(angka) {
    const number_string = angka.replace(/[^,\d]/g, '').toString();
    const split = number_string.split(',');
    const sisa = split[0].length % 3;
    let rupiah = split[0].substr(0, sisa);
    const ribuan = split[0].substr(sisa).match(/\d{3}/gi);

    if (ribuan) {
      const separator = sisa ? '.' : '';
      rupiah += separator + ribuan.join('.');
    }

    rupiah = split[1] !== undefined ? rupiah + ',' + split[1] : rupiah;
    return rupiah;
  }


/**
* Inisialisasi fungsi capture dan retake foto
* @param {string} questionId - ID unik elemen pertanyaan
*/
function initializePhotoCapture(questionId) {
  const video = document.getElementById(`video_${questionId}`);
  const videoContainer = document.getElementById(`video-container-${questionId}`);
  const photoPreviewContainer = document.getElementById(`photo-preview-container-${questionId}`);
  const canvas = document.getElementById(`canvas_${questionId}`);
  const retakeButton = document.getElementById(`retake-button-${questionId}`);
  const photoInput = document.getElementById(`photo_input_${questionId}`);
  let stream = null;

  // Function to start the camera
  function startCamera() {
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
          navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
              .then(function (videoStream) {
                  stream = videoStream;
                  video.srcObject = stream;
                  video.play();
              })
              .catch(function (err) {
                  console.error("Gagal membuka kamera:", err);
                  alert("Gagal membuka kamera. Pastikan browser Anda mengizinkan akses kamera.");
              });
      } else {
          alert("Browser ini tidak mendukung akses kamera.");
      }
  }

  // Start the camera on initialization
  startCamera();

  // Capture photo
  window.capturePhoto = function (id) {
      if (id !== questionId) return; // Ensure the function is executed for the correct ID

      const context = canvas.getContext('2d');
      context.drawImage(video, 0, 0, canvas.width, canvas.height);

      photoPreviewContainer.style.display = 'block';
      videoContainer.style.display = 'none';
      retakeButton.style.display = 'inline-block';

      const photoDataUrl = canvas.toDataURL('image/png');
      photoInput.value = photoDataUrl;
      alert('Foto berhasil diambil dan siap diunggah.');
  };

  // Retake photo
  window.retakePhoto = function (id) {
      if (id !== questionId) return; // Ensure the function is executed for the correct ID

      const context = canvas.getContext('2d');
      context.clearRect(0, 0, canvas.width, canvas.height);
      photoInput.value = '';

      photoPreviewContainer.style.display = 'none';
      videoContainer.style.display = 'block';
      retakeButton.style.display = 'none';

      if (!stream || stream.getTracks().every(track => track.readyState === 'ended')) {
          startCamera();
      }
  };

  // Clean up the camera stream on page unload
  window.addEventListener('beforeunload', function () {
      if (stream) {
          stream.getTracks().forEach(track => track.stop());
      }
  });
}
/**
* Inisialisasi canvas tanda tangan
* @param {string} questionId - ID unik elemen pertanyaan
*/
function initializeSignatureCanvas(questionId) {
  const canvas = document.getElementById(`signature-canvas-${questionId}`);
  const ctx = canvas.getContext('2d');
  let isDrawing = false;

  // Event listener untuk mulai menggambar
  canvas.addEventListener('mousedown', function (e) {
      isDrawing = true;
      ctx.beginPath();
      ctx.moveTo(e.offsetX, e.offsetY);
  });

  // Event listener untuk menggambar
  canvas.addEventListener('mousemove', function (e) {
      if (isDrawing) {
          ctx.lineTo(e.offsetX, e.offsetY);
          ctx.strokeStyle = "#000";
          ctx.lineWidth = 2;
          ctx.stroke();
      }
  });

  // Event listener untuk berhenti menggambar
  canvas.addEventListener('mouseup', function () {
      isDrawing = false;
      ctx.closePath();
  });
}

/**
* Simpan tanda tangan dari canvas ke input hidden
* @param {string} questionId - ID unik elemen pertanyaan
*/
function saveSignature(questionId) {
  const canvas = document.getElementById(`signature-canvas-${questionId}`);
  const input = document.getElementById(`question_${questionId}`);
  const signatureDataUrl = canvas.toDataURL('image/png');
  input.value = signatureDataUrl;
  alert('Tanda tangan berhasil disimpan!');
}

/**
* Bersihkan canvas tanda tangan
* @param {string} questionId - ID unik elemen pertanyaan
*/
function clearCanvas(questionId) {
  const canvas = document.getElementById(`signature-canvas-${questionId}`);
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  document.getElementById(`question_${questionId}`).value = '';
}