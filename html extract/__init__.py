def table_extract(html: str) -> dict[bool:dict[str:list]]:
    status = True
    extract = dict()
    error = dict()

    html_remove_blank = html.replace("\n", "").replace("\r", "").replace(" ", "").replace("   ", "")
    tr_start_str = "<tr>"
    tr_stop_str = "</tr>"
    tr_start_index = len(tr_start_str)
    tr_stop_index = -len(tr_stop_str)
    th_start_str = "<th>"
    th_stop_str = "</th>"
    th_start_index = len(th_start_str)
    th_stop_index = -len(th_stop_str)
    td_start_str = "<td>"
    td_stop_str = "</td>"
    td_start_index = len(td_start_str)
    td_stop_index = -len(td_stop_str)

    # remove table markup
    table_start_str = "<table>"
    table_stop_str = "</table>"
    table_start_index = len(table_start_str)
    table_stop_index = -len(table_stop_str)
    if html_remove_blank[:table_start_index] == table_start_str and html_remove_blank[
                                                                    table_stop_index:] == table_stop_str:
        html_remove_table = html_remove_blank[table_start_index:table_stop_index]
        # print(html_remove_table)
        table_split = "</table><table>"
        table_list = html_remove_table.split(table_split)
        # print(table_list)

        for i in table_list:
            # remove thead markup
            thead_start_str = "<thead>"
            thead_stop_str = "</thead>"
            thead_start_index = len(thead_start_str)
            thead_stop_index = -len(thead_stop_str)
            if thead_start_str in i and thead_stop_str in i.split(thead_start_str)[1]:
                thead = i.split(thead_start_str)[1].split(thead_stop_str)[0]
                # print(thead)

                # remove tr markup
                thead_remove_tr = thead
                if thead[:tr_start_index] == tr_start_str and thead[tr_stop_index:] == tr_stop_str:
                    thead_remove_tr = thead[tr_start_index:tr_stop_index]
                    # print(thead_remove_tr)
                    tr_split = "</tr><tr>"
                    tr_list = thead_remove_tr.split(tr_split)
                    thead_list = list()
                    for j in tr_list:
                        # remove th markup
                        thead_remove_tr_th = j
                        if j[:th_start_index] == th_start_str and j[th_stop_index:] == th_stop_str:
                            thead_remove_tr_th = j[th_start_index:th_stop_index]
                            # print(thead_remove_tr_th)
                        # print(thead_remove_tr_th)
                        th_list = thead_remove_tr_th.split("</th><th>")
                        # print(th_list)
                        thead_list.append(th_list)
                    # print(thead_list)
                    extract["thead"] = thead_list

            # remove tbody markup
            tbody_start_str = "<tbody>"
            tbody_stop_str = "</tbody>"
            tbody_start_index = len(tbody_start_str)
            tbody_stop_index = -len(tbody_stop_str)
            if tbody_start_str in i and tbody_stop_str in i.split(tbody_start_str)[1]:
                tbody = i.split(tbody_start_str)[1].split(tbody_stop_str)[0]
                # print(tbody)

                # remove tr markup
                tbody_remove_tr = tbody
                if tbody[:tr_start_index] == tr_start_str and tbody[tr_stop_index:] == tr_stop_str:
                    tbody_remove_tr = tbody[tr_start_index:tr_stop_index]
                    # print(tbody_remove_tr)
                    tr_split = "</tr><tr>"
                    tr_list = tbody_remove_tr.split(tr_split)
                    tbody_list = list()
                    for j in tr_list:
                        # remove td markup
                        tbody_remove_tr_td = j
                        if j[:td_start_index] == td_start_str and j[td_stop_index:] == td_stop_str:
                            tbody_remove_tr_td = j[td_start_index:td_stop_index]
                            # print(tbody_remove_tr_td)
                        # print(tbody_remove_tr_td)
                        td_list = tbody_remove_tr_td.split("</td><td>")
                        # print(td_list)
                        tbody_list.append(td_list)
                    # print(tbody_list)
                    extract["tbody"] = tbody_list
    else:
        status = False
        error_table_format = "Incorrect table format"
        # print(error_table_format)
        error["0"] = error_table_format

    if status:
        return {status: extract}
    else:
        return {status: error}


if __name__ == "__main__":
    html = """
    <table>
    <thead>
    <tr>
    <th>auto</th>
    <th>enum</th>
    <th>unsigned</th>
    <th>break</th>
    <th>extern</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>return</td>
    <td>void</td>
    <td>case</td>
    <td>float</td>
    <td>short</td>
    </tr>
    <tr>
    <td>volatile</td>
    <td>char</td>
    <td>for</td>
    <td>signed</td>
    <td>while</td>
    </tr>
    <tr>
    <td>const</td>
    <td>goto</td>
    <td>sizeof</td>
    <td>continue</td>
    <td>if</td>
    </tr>
    <tr>
    <td>static</td>
    <td>default</td>
    <td>struct</td>
    <td>do</td>
    <td>int</td>
    </tr>
    <tr>
    <td>switch</td>
    <td>double</td>
    <td>long</td>
    <td>typedef</td>
    <td>else</td>
    </tr>
    <tr>
    <td>register</td>
    <td>union</td>
    <td></td>
    <td></td>
    <td></td>
    </tr>
    <tr>
    <td><em>restrict</em></td>
    <td><em>inline</em></td>
    <td><em>_Bool</em></td>
    <td><em>_Complex</em></td>
    <td><em>_Imaginary</em></td>
    </tr>
    </tbody>
    </table>
    """
    result: dict = table_extract(html)
    # print(result)
    for i, j in result.items():
        for k, l in j.items():
            print(k, l)
