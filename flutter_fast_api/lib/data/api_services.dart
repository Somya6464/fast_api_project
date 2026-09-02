import 'dart:convert';
import 'dart:developer';
import 'package:flutter_fast_api/data/sharedpreference_helper.dart';
import 'package:flutter_fast_api/model/book_list_model.dart';
import 'package:flutter_fast_api/model/login_response.dart';
import 'package:http/http.dart' as http;

class BookApiService {
  // final String baseUrl = "https://fast-api-project-z7yg.onrender.com/";
  // final String baseUrl = "http://127.0.0.1:8000/";
  final String baseUrl = "http://10.0.2.2:8000/";

  Future<AuthResponse> login(String username, String password) async {
    try {
      log("api endpoint: ${baseUrl}auth/login");

      final response = await http.post(
        Uri.parse('${baseUrl}auth/login'),
        body: {'email': username, 'password': password},
      );
      log("response: ${response.body}");

      if (response.statusCode == 200) {
        final authResponseModel = AuthResponse.fromJson(
          jsonDecode(response.body),
        );
        await LocalStorageHelper.saveToken(
          authResponseModel.accessToken,
          authResponseModel.tokenType,
        );
        await LocalStorageHelper.saveUser(authResponseModel.user);
        return authResponseModel;
      }
      throw Exception('Login failed: ${response.statusCode}');
    } catch (e) {
      throw Exception('Login error: ${e.toString()}');
    }
  }

  Future<void> signup({
    required String username,
    required String email,
    required String password,
    required String role,
  }) async {
    try {
      log("api endpoint: ${baseUrl}auth/signup");

      final response = await http.post(
        Uri.parse('${baseUrl}auth/signup'),

        body: {
          "username": username,
          "email": email,
          "password": password,
          "role": role,
        },
      );

      log("response: ${response.body}");

      if (response.statusCode == 200 || response.statusCode == 201) {
        return;
      }

      throw Exception("Signup failed");
    } catch (e) {
      throw Exception("Signup error: ${e.toString()}");
    }
  }

  Future<AuthResponse> verifyOtp({
    required String email,
    required String otp,
  }) async {
    try {
      final response = await http.post(
        Uri.parse('${baseUrl}auth/verify-otp'),
        body: {"email": email, "otp": otp},
      );

      return AuthResponse.fromJson(jsonDecode(response.body));
    } catch (e) {
      throw Exception("OTP verification failed");
    }
  }

  Future<void> resendOtp(String email) async {
    try {
      await http.post(
        Uri.parse('${baseUrl}auth/resend-otp'),
        body: {"email": email},
      );
    } catch (e) {
      throw Exception("Unable to resend OTP");
    }
  }

  /* Future<Options> _authorizedOptions() async {
    final token = await LocalStorageHelper.getToken();

    if (token == null || token.isEmpty) {
      throw Exception("User is not logged in.");
    }

    return Options(
      headers: {
        "Authorization": "Bearer $token",
        "Content-Type": Headers.jsonContentType,
      },
    );
  } */

  Future<List<BookListResponse>> getBooks() async {
    try {
      log("api endpoint: ${baseUrl}books/get_books");
      final response = await http.get(Uri.parse("${baseUrl}books/get_books"));
      log("response: ${response.body}");
      if (response.statusCode == 200) {
        final List<dynamic> data = jsonDecode(response.body);
        return data.map((json) => BookListResponse.fromJson(json)).toList();
      }
      throw Exception('Failed to load books: ${response.statusCode}');
    } catch (e) {
      throw Exception('Network error: ${e.toString()}');
    }
  }

  Future<bool> deleteBook(int bookId) async {
    try {
      log("api endpoint: ${baseUrl}books/delete_book/$bookId");
      final response = await http.delete(
        Uri.parse('${baseUrl}books/delete_book/$bookId'),
        // options: await _authorizedOptions(),
      );
      log("response: ${response.body}");
      return response.statusCode == 200 || response.statusCode == 204;
    } catch (e) {
      throw Exception('Failed to delete book: ${e.toString()}');
    }
  }

  Future<BookListResponse> updateBook(int bookId, BookListResponse book) async {
    try {
      log("api endpoint: ${baseUrl}books/update_book/$bookId");
      log(
        "request body: ${jsonEncode({'title': book.title, 'description': book.description, 'author': book.author, 'year': book.year})}",
      );
      final response = await http.put(
        Uri.parse('${baseUrl}books/update_book/$bookId'),
        headers: {"Content-Type": "application/json"},
        // options: await _authorizedOptions(),
        body: jsonEncode({
          'title': book.title,
          'description': book.description,
          'author_id': book.authorId,
          'author': book.author,
          'year': book.year,
        }),
      );
      log("response: ${response.body}");

      if (response.statusCode == 200) {
        return BookListResponse.fromJson(jsonDecode(response.body));
      }
      throw Exception('Failed to update book');
    } catch (e) {
      throw Exception('Failed to update book: ${e.toString()}');
    }
  }

  Future<BookListResponse> createBook(BookListResponse book) async {
    try {
      log("api endpoint: ${baseUrl}books/create_book");
      log(
        "request body: ${jsonEncode({'title': book.title, 'description': book.description, 'author_id': book.authorId, 'author': book.author, 'year': book.year})}",
      );
      final response = await http.post(
        Uri.parse('${baseUrl}books/create_book'),
        headers: {"Content-Type": "application/json"},
        // options: await _authorizedOptions(),
        body: jsonEncode({
          'title': book.title,
          'description': book.description,
          'author_id': book.authorId,
          'author': book.author,
          'year': book.year,
        }),
      );
      log("response: ${response.body}");

      if (response.statusCode == 200 || response.statusCode == 201) {
        return BookListResponse.fromJson(jsonDecode(response.body));
      }
      throw Exception('Failed to create book');
    } catch (e) {
      throw Exception('Failed to create book: ${e.toString()}');
    }
  }

  Future<void> callUnprotectedApi() async {
    try {
      log("api endpoint: http://jsonplaceholder.typicode.com/posts");
      final response = await http.get(
        Uri.parse('http://jsonplaceholder.typicode.com/posts'),
        // options: await _authorizedOptions(),
      );
      log("response: ${response.body}");
      // if (response.statusCode == 200) {
      //   final List<dynamic> data = response.data;
      //   return data.map((json) => BookListResponse.fromJson(json)).toList();
      // }
      // throw Exception('Failed to load books: ${response.statusCode}');
    } catch (e) {
      throw Exception('Network error: ${e.toString()}');
    }
  }
}
