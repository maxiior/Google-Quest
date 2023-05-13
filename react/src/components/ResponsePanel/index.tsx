import "./index.scss";

const ResponsePanel = ({ response }: { response?: any }) => {
  var rows: any = [];

  if (response) {
    for (let key in response) {
      let class_name: string = "";
      if (
        ["question_title", "question_body", "answer", "category"].includes(key)
      )
        class_name = "response_container inputs";
      else class_name = "response_container";

      rows.push(
        <div className={class_name}>
          <div>{key}</div>
          <div>{response[key]}</div>
        </div>
      );
    }
  }

  return <div>{rows}</div>;
};

export default ResponsePanel;
