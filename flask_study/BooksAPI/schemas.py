# marshmallow == pydantic 데이터의 타입을 직렬화, 역직렬화 하는 라이브러리 or 데이터 검증도 가능
from marshmallow import Schema, fields


class BookSchema(Schema):
    # id 필드가 직렬화 (객체에서 Json으로 변환) 과정에만 사용 서버 -> 클라
    # 역직렬화 즉 클라 -> 서버로 오는 JSON-> 객체로 변환하는 과정에는 무시
    # 즉 id 값은 서버에서 관리
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
