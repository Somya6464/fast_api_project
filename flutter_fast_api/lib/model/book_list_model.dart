class BookListResponse {
  final int id;
  final String title;
  final String description;
  final int authorId;
  final String author;
  final int year;

  BookListResponse({
    required this.id,
    required this.title,
    required this.description,
    required this.authorId,
    required this.author,
    required this.year,
  });

  factory BookListResponse.fromJson(Map<String, dynamic> json) {
    return BookListResponse(
      id: json['id'] as int,
      title: json['title'] as String? ?? '',
      description: json['description'] as String? ?? '',
      author: json['author'] as String? ?? '',
      year: json['year'] as int? ?? 0,
      authorId: json['author_id'] as int? ?? 6
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      'description': description,
      'author': author,
      'year': year,
      'author_id': authorId
    };
  }

  BookListResponse copyWith({
    int? id,
    String? title,
    String? description,
    String? author,
    int? year,
    int? authorId
  }) {
    return BookListResponse(
      id: id ?? this.id,
      title: title ?? this.title,
      description: description ?? this.description,
      author: author ?? this.author,
      year: year ?? this.year,
      authorId: authorId ?? this.authorId
    );
  }
}
