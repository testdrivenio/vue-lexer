<template>
  <table class="table table-hover">
    <thead>
      <tr>
        <th scope="col">Title</th>
        <th scope="col">Author</th>
        <th scope="col">Read?</th>
        <th scope="col">Purchase Price</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(book, index) in books" :key="index">
        <td>{{ book.title }}</td>
        <td>{{ book.author }}</td>
        <td>
          <span v-if="book.read">Yes</span>
          <span v-else>No</span>
        </td>
        <td>${{ book.price }}</td>
        <td>
          <button type="button"
                  class="btn btn-warning btn-sm"
                  v-b-modal.book-update-modal
                  @click="editBook(book)">
              Update
          </button>
          <button type="button"
                  class="btn btn-danger btn-sm"
                  @click="onDeleteBook(book)">
              Delete
          </button>
        </td>
      </tr>
    </tbody>
  </table>
</template>
