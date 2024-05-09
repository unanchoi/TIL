
## Test
...

## Test

## Entity

```java
@Entity
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Member extends BaseTimeEntity {

    private static final int MAX_AGE = 100;
    private static final int MAX_LENGTH = 12;
    private static final short CURRENT_GENERATION = 34;
    private static final Pattern NAME_PATTERN = Pattern.compile("가-힣");

    @Id
    @GeneratedValue(strategy = IDENTITY)
    private Long id;
    private String name;
    private String nickname;
    private int age;
    private boolean isDeleted = false;

    @Embedded
    private SOPT sopt;

    @OneToMany(mappedBy = "member", cascade = CascadeType.ALL)
    private final List<Post> posts = new ArrayList<>();

    @Builder
    private Member(String name,
                   String nickname,
                   int age,
                   SOPT sopt) {
        validateAge(age);
        validateName(name);
        validateNickname(nickname);
        this.name = name;
        this.nickname = nickname;
        this.age = age;
        this.sopt = sopt;
        this.isDeleted = false;
    }

    private void validateAge(final int age) {
        if (0 > age || age > MAX_AGE) {
            throw new MemberException("회원의 나이는 0세 이상 100세 이하입니다.");
        }
    }

    // SOPT는 한국인만 가입 가능함.
    private void validateName(final String name) {
        if (NAME_PATTERN.matcher(name).matches()) {
            throw new MemberException("유저의 이름은 한글만 가능합니다.");
        }

       if (name.length() > MAX_LENGTH) {
            throw new MemberException("유저의 이름은 12자를 넘을 수 없습니다.");
       }
    }

    private void validateNickname(final String nickname) {

        if (nickname.length() > 8) {
            throw new MemberException("유저의 닉네임은 8자를 넘길 수 없습니다.");
        }
    }

    public void remove() {

        this.isDeleted = true;
    }

    public void updateSOPT(SOPT sopt) {
        this.sopt = sopt;
    }
}
```
```

## Repository Test

1. Mock
2. H2 설정 후 Test

```java
@DataJpaTest
@ActiveProfiles("test")
public class PostJpaRepositoryTest {

    @Autowired
    PostJpaRepository postJpaRepository;

    @Autowired
    MemberJpaRepository memberJpaRepository;

    @Test
    @DisplayName("사용자 이름으로 작성한 게시글을 모두 조회할 수 있다.")
    void findAllByMemberNameIn() {
      // given
        Member member1 = createMember("오해영");
        Member member2 = createMember("또오해영");
        memberJpaRepository.save(member1);
        memberJpaRepository.save(member2);
        Post post1 = createPost("제목1", "내용1", member1);
        Post post2 = createPost("제목2", "내용2", member1);
        Post post3 = createPost("제목3", "내용3", member2);
        postJpaRepository.saveAll(List.of(post1, post2, post3));

        // when
        List<Post> findPosts = postJpaRepository.findAllByMemberNameIn(List.of("오해영", "또오해영"));

        // then
         Assertions.assertThat(findPosts)
                .extracting("title", "content")
                .containsExactlyInAnyOrder(
                        Assertions.tuple("제목1", "내용1"),
                        Assertions.tuple("제목2", "내용2"),
                        Assertions.tuple("제목3", "내용3")
                );
    }

    private Post createPost(String title, String content, Member member) {
         return Post.builder()
                .title(title)
                .content(content)
                .member(member)
                .build();
    }

    private Member createMember(String name) {
        SOPT sopt = SOPT.builder()
                .part(Part.SERVER)
                .build();
        return Member.builder()
                .age(99)
                .name(name)
                .sopt(sopt)
                .nickname("5hae0")
                .build();
    }


}
```

## Service Test

