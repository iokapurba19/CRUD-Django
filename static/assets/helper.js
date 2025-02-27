document.addEventListener('DOMContentLoaded', function () {
    const deleteModal = document.getElementById('deleteModal');
    const deleteForm = document.getElementById('deleteForm');
    const entityNameSpan = document.getElementById('entityName');

    deleteModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget; // Tombol yang memicu modal
        const entityName = button.getAttribute('data-entity-name'); // Nama entitas
        const deleteUrl = button.getAttribute('data-delete-url'); // URL untuk penghapusan

        // Set nama entitas di modal
        entityNameSpan.textContent = entityName;

        // Update action form
        deleteForm.action = deleteUrl;
    });
});

$(document).ready(function () {
    $('.only-numbers').on('input', function () {
        console.log("Input detected: ", this.value); // Debugging log
        // Hapus semua karakter selain angka
        this.value = this.value.replace(/[^0-9]/g, '');
    });
});

$(document).ready(function () {
    function formatCurrency(value) {
        if (!value) return ''; // Jika tidak ada nilai, kembalikan string kosong
        // Pastikan hanya angka yang diproses
        value = value.toString().replace(/[^0-9]/g, '');
        // Format angka ke pemisah ribuan
        return new Intl.NumberFormat('id-ID').format(value);
    }

    // Terapkan format currency ke semua input dengan class `.currency-format`
    $('.currency-format').each(function () {
        let value = $(this).val(); // Ambil nilai dari input
        $(this).val(formatCurrency(value)); // Set nilai terformat kembali ke input
    });

    // Update nilai saat pengguna mengetik
    $('.currency-format').on('input', function () {
        let value = this.value.replace(/[^0-9]/g, ''); // Hapus karakter selain angka
        this.value = formatCurrency(value); // Terapkan format currency
    });
});


