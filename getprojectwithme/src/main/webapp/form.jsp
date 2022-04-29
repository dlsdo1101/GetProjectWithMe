<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width", initial-scale="1">
<link rel="stylesheet" href="css/bootstrap.css">
<link rel="stylesheet" href="css/custom.css">
</head>
<body>
	<div class="container">
		<div class="col-lg-4"></div>
		<div class="col-lg-4">
			<div class="jumbotron" style="padding-top: 20px;">
				<form method="post" action="authentication.jsp">
					<h2 style="text-align: center;" >로그인</h2>
					<div class="form-group">
						<h5>아이디</h5>
						<input name="id" class="form-control" type="text" maxlength="20">
						</div>
					<div class="form-group">
						<h5>비밀번호</h5>
						<input type="password" class="form-control" placeholder="숫자, 문자, 특수문자를 포함한 8자 이상으로 입력하세요" name="pw" maxlength="20">
						</div>
					<h1></h1>
					<input type="submit" class="btn btn-primary form-control" value="로그인">
					<h3></h3>
					<input type="submit" class="btn btn-primary form-control" value="회원가입">
				</form>
			</div>
		</div>
	</div>
</body>
</html>