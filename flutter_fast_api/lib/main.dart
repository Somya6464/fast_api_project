import 'package:flutter/material.dart';
import 'package:flutter_fast_api/data/sharedpreference_helper.dart';
import 'package:flutter_fast_api/views/book_list_page.dart';

import 'views/login_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(colorScheme: .fromSeed(seedColor: Colors.deepPurple)),
      home: AuthGate(),
    );
  }
}

/// Decides which screen to show on app launch
class AuthGate extends StatelessWidget {
  const AuthGate({super.key});

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<bool>(
      future: LocalStorageHelper.isLoggedIn(),
      builder: (context, snapshot) {
        // While checking token, show splash / loader
        if (snapshot.connectionState == ConnectionState.waiting) {
          return const Scaffold(
            body: Center(child: CircularProgressIndicator()),
          );
        }

        // If token exists → BookListPage, else → LoginScreen
        if (snapshot.data == true) {
          return const BookListPage();
        }
        return const LoginScreen();
      },
    );
  }
}
